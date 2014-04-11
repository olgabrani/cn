# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'excercise_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('semester', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'excercise', ['Course'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'excercise_course')


    models = {
        u'excercise.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['excercise']