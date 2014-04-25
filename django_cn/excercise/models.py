# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

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

    def __unicode__(self):
        return self.title

class Question(models.Model):
    
    ANSWER_TYPE_CHOICES = (
        ('T', 'Text'),
        ('I', 'Image File'),
        ('L', 'Link')
    )

    text = models.TextField(null=True, blank=True)
    order = models.CharField(max_length=32)
    suggested_answer = models.TextField(null=True, blank=True)
    answer_type = models.CharField(max_length=1, choices=ANSWER_TYPE_CHOICES,default='T')
    exercise = models.ForeignKey(Exercise)
    
    def __unicode__(self):
        return self.text[0:256]

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
            print course_codes
            enrolled_courses = Course.objects.filter(code__in=course_codes)
            return enrolled_courses
