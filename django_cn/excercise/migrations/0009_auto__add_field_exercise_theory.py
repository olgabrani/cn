# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Exercise.theory'
        db.add_column(u'excercise_exercise', 'theory',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Exercise.theory'
        db.delete_column(u'excercise_exercise', 'theory')


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
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 14, 0, 0)'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'theory': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'excercise.question': {
            'Meta': {'object_name': 'Question'},
            'answer_type': ('django.db.models.fields.CharField', [], {'default': "'T'", 'max_length': '1'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'suggested_answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['excercise']