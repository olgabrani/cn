# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, date

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
    course = models.ForeignKey(Course)
    release_date = models.DateField(default=datetime.now())
    is_active = models.BooleanField()
    number = models.PositiveIntegerField()

    def __unicode__(self):
        return self.title

