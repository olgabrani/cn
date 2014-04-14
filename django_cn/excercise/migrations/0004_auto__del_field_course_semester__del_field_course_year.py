# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Course.semester'
        db.delete_column(u'excercise_course', 'semester')

        # Deleting field 'Course.year'
        db.delete_column(u'excercise_course', 'year')


    def backwards(self, orm):
        # Adding field 'Course.semester'
        db.add_column(u'excercise_course', 'semester',
                      self.gf('django.db.models.fields.CharField')(default='S', max_length=1),
                      keep_default=False)

        # Adding field 'Course.year'
        db.add_column(u'excercise_course', 'year',
                      self.gf('django.db.models.fields.CharField')(default=2014, max_length=128),
                      keep_default=False)


    models = {
        u'excercise.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'excercise.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 13, 0, 0)'}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['excercise']