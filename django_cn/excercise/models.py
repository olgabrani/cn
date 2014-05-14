# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

def submission_list(course_code=None, exercise_number=None, group_id=None, filtering=None):
    if filtering == 'corrected':
        submissions = Submission.objects.filter(state='C')
    elif filtering == 'all':
        submissions = Submission.objects.all()
    else: 
        submissions = Submission.objects.filter(state='S')
    if course_code:
        submissions = submissions.filter(exercise__course__code=course_code)
    if  exercise_number and int(exercise_number) > 0:
        submissions = submissions.filter(exercise__number=exercise_number)
    if group_id:
        groupmembers = MdlGroupsMembers.objects.using('users').filter(groupid=group_id)
        mdlusers_ids = []
        for g in groupmembers:
            mdlusers_ids.append(g.userid)
        mdlusers = MdlUser.objects.using('users').filter(pk__in = mdlusers_ids)
        usernames = []
        for m in mdlusers:
            usernames.append(m.username)
        submissions = submissions.filter(student__username__in=usernames)
    return submissions


class Course(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64)

    @property
    def school_year(self):
        try:
            year = int(self.code[-4:])
        except:
            year = date.today().year
        next_year = year+1
        return '%d-%d' % (year, next_year)
   
    @property
    def exercises(self):
        return self.exercise_set.filter(is_active=True)
    
    def get_group(self, user):

        userid = MdlUser.objects.using('users').get(username=user.username).pk
        try:
            groupid = MdlGroupsMembers.objects.using('users').get(userid=userid).groupid
            try: 
                courseid = MdlCourse.objects.using('users').get(shortname=self.code).pk
                group = MdlGroups.objects.using('users').get(pk=groupid, courseid=courseid)
            except:
                group = None
        except: 
            group = None

        return group 

    @property
    def get_groups(self):
        
        try: 
            courseid = MdlCourse.objects.using('users').get(shortname=self.code).pk
        except:
            courseid = None

        groups = MdlGroups.objects.using('users').filter(courseid=courseid)
        return groups

    def cnt_submissions(self,filtering=None):
        cnt_submissions = 0
        submissions = submission_list(self.code, None, None, filtering)
        if submissions:
            cnt_submissions = submissions.count()
        return cnt_submissions

    @property
    def cnt_subm_corrected(self):
        return self.cnt_submissions(filtering='corrected')

    @property
    def cnt_subm_submitted(self):
        return self.cnt_submissions()
    

    def __unicode__(self):
        return self.name + ' ( Code:' + self.code +' )'


class Exercise(models.Model):
    title = models.TextField()
    subtitle = models.TextField(null=True, blank=True)
    theory = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course)
    release_date = models.DateField(default=datetime.now())
    is_active = models.BooleanField()
    number = models.PositiveIntegerField()

    @property
    def questions(self):
        return self.question_set.all()

    @property
    def course_code(self):
        return self.course.code

    def submission_code(self, user):
        try:
            submission_code = Submission.objects.get(exercise = self, student = user).state
        except:
            submission_code = 'O'
        return submission_code


    def submission_state(self, user):

        dict = {'I': 'Ημιτελής', 'C': 'Διορθωμένη', 'S': 'Υπεβλήθη'}
        try:
            submission_obj = Submission.objects.get(exercise = self, student=user).state
            submission = dict.get(submission_obj)
        except:
            submission = 'Ανοιχτή'
        return submission    

    def cnt_submissions(self, group_id=None, filtering=None):
        cnt = 0
        code = self.course_code
        submissions = submission_list(code, self.number, group_id, filtering)
        if submissions:
            cnt = submissions.count()
        return cnt


    def __unicode__(self):
        return self.title

class Question(models.Model):
    ANSWER_TYPE_CHOICES = (
        ('T', 'Text'),
        ('I', 'Image File'),
        ('L', 'Link'),
        ('E', 'Empty')
    )
    #Empty option can be used for theory
    text = models.TextField(null=True, blank=True)
    order = models.CharField(max_length=32)
    suggested_answer = models.TextField(null=True, blank=True)
    answer_type = models.CharField(max_length=1, choices=ANSWER_TYPE_CHOICES,default='T')
    exercise = models.ForeignKey(Exercise)
    
    def __unicode__(self):
        return self.text[0:256]

class Answer(models.Model):
    question = models.ForeignKey(Question)
    student = models.ForeignKey(User)
    answer = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.question.order+' Student: ' +self.student.username

    class Meta:
        managed = False

class Submission(models.Model):
    SUBMISSION_STATE = (
        ('I', 'incomplete'),
        ('S', 'submitted'),
        ('C', 'corrected'),
    )
    

    exercise = models.ForeignKey(Exercise)
    student = models.ForeignKey(User)
    datetime_submitted = models.DateTimeField(null=True, blank=True)
    datetime_corrected = models.DateTimeField(null=True, blank=True)
    state = models.CharField(max_length=1, choices = SUBMISSION_STATE, default='I')
    grade = models.CharField(max_length=2, null=True, blank=True)

    @property
    def group_id(self):
        userid = MdlUser.objects.using('users').get(username=self.student.username).pk
        group_id = MdlGroupsMembers.objects.using('users').get(userid=userid).pk
        return group_id

    def __unicode__(self):
        return self.student.username


class MdlUser(models.Model):
    confirmed = models.IntegerField()
    deleted = models.IntegerField()
    suspended = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
   
    def is_enrolled(self, course_code):
        return self.username
   

    class Meta:
        managed = False
        db_table = 'mdl_user'

class MdlCourse(models.Model):
    shortname = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
        
    class Meta:
        managed = False
        db_table = 'mdl_course'

class MdlUserEnrolments(models.Model):
    status = models.BigIntegerField()
    enrolid = models.BigIntegerField()
    userid = models.BigIntegerField()
    
    @property
    def course_code(self):
        courseid = MdlEnrol.objects.using('users').get(pk=self.enrolid).courseid
        course_code = MdlCourse.objects.using('users').get(pk=courseid).shortname
        return course_code

    class Meta:
        managed = False
        db_table = 'mdl_user_enrolments'

class MdlEnrol(models.Model):
    enrol = models.CharField(max_length=20)
    status = models.BigIntegerField()
    courseid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol'

class MdlGroups(models.Model):
    courseid = models.BigIntegerField()
    name = models.CharField(max_length=254)
   
    class Meta:
        managed = False
        db_table = 'mdl_groups'

class MdlGroupsMembers(models.Model):
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
                            
    class Meta:
        managed = False
        db_table = 'mdl_groups_members'

class ProxyUser(User):
    class Meta:
        proxy = True

    @property
    def is_moodle_user(self):
        return MdlUser.objects.using('users').get(username=self.username)

    @property
    def enrolled_courses(self):
        if self.is_moodle_user:
            course_codes = []
            enrolments = MdlUserEnrolments.objects.using('users').filter(userid=self.is_moodle_user.pk)
            for e in enrolments:
                course_codes.append(e.course_code)
            enrolled_courses = Course.objects.filter(code__in=course_codes)
            for e in enrolled_courses:
                e.group = e.get_group(self)
            return enrolled_courses
