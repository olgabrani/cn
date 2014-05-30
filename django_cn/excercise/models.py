# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from filebrowser.fields import FileBrowseField

def submission_list(course_code=None, exercise_number=None, group_id=None, filtering=None):
    if filtering == 'corrected':
        submissions = Submission.objects.filter(state='C')
    elif filtering == 'all':
        submissions = Submission.objects.exclude(state='I')
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

class Application(models.Model):

    title = models.CharField(max_length=255, blank=False, null=False)
    tab_title = models.CharField(max_length=255, blank=False, null=False)
    footer_content = models.TextField(default="",blank=True)
    extra_styles = models.TextField(default="",blank=True)
    info = models.TextField(default="",blank=True)

    @classmethod
    def current(cls):
        return cls.objects.get(pk=1)

    def __unicode__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

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
    
    @property
    def moodle_course_id(self):
        try: 
            courseid = MdlCourse.objects.using('users').get(shortname=self.code).pk
        except:
            courseid = None
        return courseid
    

    @property
    def get_groups(self):
        groups = MdlGroups.objects.using('users').filter(courseid=self.moodle_course_id)
        return groups
    
    @property
    def cnt_subm_corrected(self):
        return self.cnt_submissions(filtering='corrected')

    @property
    def cnt_subm_submitted(self):
        return self.cnt_submissions()
    

    @property
    def submissions(self):
        return submission_list(self.code, 0, None, 'corrected')

    @property
    def student_list(self):
        return User.objects.filter(submission=self.submissions).select_related().distinct()

    # course teachers are found through moodle enrolements
    @property
    def teachers(self):
        moodle_course_id = self.moodle_course_id
        mdl_enrol = MdlEnrol.objects.using('users').filter(courseid=moodle_course_id)
        enrolid = []
        for m in mdl_enrol:
            enrolid.append(m.pk)
        userenrolements = MdlUserEnrolments.objects.using('users').filter(enrolid__in=enrolid)
        users = []
        for u in userenrolements:
            if u.is_teacher:
                users.append(u.userid)
        teachers = MdlUser.objects.using('users').filter(pk__in=users)
        res = []
        for t in teachers:
            res.append(t.fullname)
        return res

    # Returns all active courses
    @classmethod
    def active_courses(cls):
        return cls.objects.filter(is_active=True)

    # Returns all active courses with given course code
    @classmethod
    def get_course(cls,code):
        return cls.active_courses().get(code=code)


    def is_course_teacher(self, moodle_user):
        userid = moodle_user.pk
        contextid = MdlContext.objects.using('users').filter(instanceid=self.moodle_course_id)
        try:
            res = MdlRoleAssignments.objects.using('users').get(contextid__in=contextid, roleid=settings.TEACHER_ROLE_ID, userid=userid)
            return True
        except:
            return False


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

    def get_group_name(self,user):
        group_name = ''
        if self.get_group(user):
            group_name = self.get_group(user).name
        return group_name

    def cnt_submissions(self,filtering=None):
        cnt_submissions = 0
        submissions = submission_list(self.code, None, None, filtering)
        if submissions:
            cnt_submissions = submissions.count()
        return cnt_submissions

        
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
    document = FileBrowseField("PDF", max_length=200, directory="pdf/", extensions=[".pdf",".doc", ".docx"], blank=True, null=True)

    @property
    def questions(self):
        return self.question_set.all()

    @property
    def course_code(self):
        return self.course.code

    # Get exercise instance by given parameters and return selected questions as well
    @classmethod
    def get_exercise(cls,course,number):
        return cls.objects.select_related('questions').get(course=course, number=number)

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
        return '%d: %s (%s)' %(self.number, self.title, self.course_code)

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
    img = models.ImageField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

    @classmethod
    def get_answer(cls,question,student):
        try:
            ans = cls.objects.get(question=question, student=student)
            return ans
        except:
            return ''

    def __unicode__(self):
        return self.question.order+' Student: ' +self.student.username


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
    examiner = models.ForeignKey(User, related_name="submission_examiner",null=True, blank=True)

    @property
    def group_id(self):
        userid = MdlUser.objects.using('users').get(username=self.student.username).pk
        group_id = MdlGroupsMembers.objects.using('users').get(userid=userid).pk
        return group_id
    
    @classmethod
    def get_submission(cls, exercise, student):
        return cls.objects.get(exercise=exercise, student=student)

    def __unicode__(self):
        return self.student.username

class Grade(models.Model):

    course = models.ForeignKey(Course)
    student = models.ForeignKey(User)
    datetime_submitted = models.DateTimeField(auto_now=True)
    grade = models.CharField(max_length=2, null=True, blank=True)
    examiner = models.ForeignKey(User, related_name="grades_examiner",null=True, blank=True)

    @classmethod
    def get_or_create_grade(cls,course,student):
        return cls.objects.get_or_create(course=course,student=student)
    
    def __unicode__(self):
        return "%s (%s) Grade: %s" % (self.student, self.course, self.grade) 

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
   
    @property
    def fullname(self):
        return "%s %s" % (self.firstname, self.lastname)

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

    def is_role(self, role_id):
        courseid = MdlEnrol.objects.using('users').get(pk=self.enrolid).courseid
        contexts = MdlContext.objects.using('users').filter(instanceid=courseid)
        c_ids = []
        for c in contexts:
            c_ids.append(c.pk)
        try: 
            r = MdlRoleAssignments.objects.using('users').get(roleid=role_id,contextid__in=c_ids, userid=self.userid)
            return True
        except:
            return False

    @property
    def is_student(self):
        return self.is_role(settings.STUDENT_ROLE_ID)
    
    @property
    def is_examiner(self):
        return self.is_role(settings.EXAMINER_ROLE_ID) or self.is_role(settings.TEACHER_ROLE_ID)
    
    @property
    def is_teacher(self):
        return self.is_role(settings.TEACHER_ROLE_ID)
       
  
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

class MdlRoleAssignments(models.Model):
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    userid = models.BigIntegerField()
    
    class Meta:
        managed = False
        db_table = 'mdl_role_assignments'

class MdlContext(models.Model):
    instanceid = models.BigIntegerField()
    
    class Meta:
        managed = False
        db_table = 'mdl_context'



class ProxyUser(User):
    class Meta:
        proxy = True

    @property
    def is_moodle_user(self):
        return MdlUser.objects.using('users').get(username=self.username)

    @property
    def moodle_fullname(self):
        return self.is_moodle_user.fullname
    
    def enrolled_courses_role(self, role):
        if self.is_moodle_user:
            course_codes = []
            enrolments = MdlUserEnrolments.objects.using('users').filter(userid=self.is_moodle_user.pk)
            for e in enrolments:
                if role == 'student':
                    if e.is_student:
                        course_codes.append(e.course_code)
                if role == 'examiner':
                    if e.is_examiner:
                        course_codes.append(e.course_code)
            enrolled_courses = Course.objects.filter(code__in=course_codes, is_active=True)
            for e in enrolled_courses:
                e.group = e.get_group(self)
                e.user_is_course_teacher = e.is_course_teacher(self.is_moodle_user)
            return enrolled_courses

    
    # for students
    @property
    def enrolled_courses(self):
        return self.enrolled_courses_role('student') 

    # for examiners
    @property
    def enrolled_courses_examiner(self):
        return self.enrolled_courses_role('examiner') 
