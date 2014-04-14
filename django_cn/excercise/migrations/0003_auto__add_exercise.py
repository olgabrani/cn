# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exercise'
        db.create_table(u'excercise_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['excercise.Course'])),
            ('release_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 4, 13, 0, 0))),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'excercise', ['Exercise'])


    def backwards(self, orm):
        # Deleting model 'Exercise'
        db.delete_table(u'excercise_exercise')


    models = {
        u'excercise.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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