# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, date
from django.forms import fields
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from filebrowser.fields import FileBrowseField

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^excercise\.models\.MACAddressField"])

MAC_RE = r'^([0-9a-fA-F]{2}([:-]?|$)){6}$'
mac_re = re.compile(MAC_RE)

class MACAddressFormField(fields.RegexField):
    default_error_messages = {
        'invalid': _(u'Eισάγετε μια έγκυρη MAC address.'),
    }
    
    def __init__(self, *args, **kwargs):
        super(MACAddressFormField, self).__init__(mac_re, *args, **kwargs)

class MACAddressField(models.Field):
    empty_strings_allowed = False
                                    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 17
        super(MACAddressField, self).__init__(*args, **kwargs)
    
    def get_internal_type(self):
        return "CharField"

    def formfield(self, **kwargs):
        defaults = {'form_class': MACAddressFormField}
        defaults.update(kwargs)
        return super(MACAddressField, self).formfield(**defaults)


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
    
    SEMESTERS = (
        ('E', 'Summer'),
        ('W', 'Winter'),
    )
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64)
    semester = models.CharField(max_length=1, choices=SEMESTERS, default='E')
    is_active = models.BooleanField(default=True)

    @property
    def school_year(self):
        try:
            year = int(self.code[-4:])
        except:
            year = date.today().year
        next_year = year+1
        last_year = year-1
        if self.semester == 'E':
           return '%d-%d' % (last_year, year)
        else:
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
        return ', '.join(res)

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

        dict = {'I': 'Ημιτελής', 'C': 'Υπεβλήθη', 'S': 'Υπεβλήθη'}
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
        ('E', 'Empty')
    )
    #Empty option can be used for theory
    text = models.TextField(null=True, blank=True)
    order = models.CharField(max_length=32)
    suggested_answer = models.TextField(null=True, blank=True)
    answer_type = models.CharField(max_length=1, choices=ANSWER_TYPE_CHOICES,default='T')
    exercise = models.ForeignKey(Exercise)
    
    @classmethod
    def get_question(cls,question_id):
        try:
            q = cls.objects.get(pk=question_id)
            return q
        except:
            return ''


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
    #ip is the IP claimed by the user
    ip = models.GenericIPAddressField(null=True, blank=True)
    #calculated_ip is the IP automattically inserted upon submission
    calculated_ip = models.GenericIPAddressField(null=True, blank=True)
    mac_address = MACAddressField(null=True, blank=True)
    pc_name = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    
    
    @property
    def group_id(self):
        userid = MdlUser.objects.using('users').get(username=self.student.username).pk
        group_id = MdlGroupsMembers.objects.using('users').get(userid=userid).pk
        return group_id
    
    @classmethod
    def get_submission(cls, exercise, student):
        return cls.objects.get(exercise=exercise, student=student)
    
    @classmethod
    def get_or_create_submission(cls, exercise, student):
        return cls.objects.get_or_create(exercise=exercise, student=student)


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