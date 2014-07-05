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




