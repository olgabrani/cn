# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Suggested'
        db.create_table(u'parsing_suggested', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['excercise.Exercise'])),
            ('purge', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('document', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
        ))
        db.send_create_signal(u'parsing', ['Suggested'])


    def backwards(self, orm):
        # Deleting model 'Suggested'
        db.delete_table(u'parsing_suggested')


    models = {
        u'excercise.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'excercise.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Course']"}),
            'document': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 22, 0, 0)'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'theory': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'parsing.parse': {
            'Meta': {'object_name': 'Parse'},
            'document': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purge': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'parsing.suggested': {
            'Meta': {'object_name': 'Suggested'},
            'document': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purge': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['parsing']