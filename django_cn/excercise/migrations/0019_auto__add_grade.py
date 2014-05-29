# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grade'
        db.create_table(u'excercise_grade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['excercise.Course'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('datetime_submitted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('examiner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'grades_examiner', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'excercise', ['Grade'])


    def backwards(self, orm):
        # Deleting model 'Grade'
        db.delete_table(u'excercise_grade')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'excercise.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Question']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'excercise.application': {
            'Meta': {'object_name': 'Application'},
            'extra_styles': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'footer_content': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'tab_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
            'release_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 28, 0, 0)'}),
            'subtitle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'theory': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'excercise.grade': {
            'Meta': {'object_name': 'Grade'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Course']"}),
            'datetime_submitted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'examiner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'grades_examiner'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'excercise.mdlcontext': {
            'Meta': {'object_name': 'MdlContext', 'db_table': "u'mdl_context'", 'managed': 'False'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instanceid': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'excercise.mdlcourse': {
            'Meta': {'object_name': 'MdlCourse', 'db_table': "u'mdl_course'", 'managed': 'False'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idnumber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'excercise.mdlenrol': {
            'Meta': {'object_name': 'MdlEnrol', 'db_table': "u'mdl_enrol'", 'managed': 'False'},
            'courseid': ('django.db.models.fields.BigIntegerField', [], {}),
            'enrol': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'excercise.mdlgroups': {
            'Meta': {'object_name': 'MdlGroups', 'db_table': "u'mdl_groups'", 'managed': 'False'},
            'courseid': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'excercise.mdlgroupsmembers': {
            'Meta': {'object_name': 'MdlGroupsMembers', 'db_table': "u'mdl_groups_members'", 'managed': 'False'},
            'groupid': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'userid': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'excercise.mdlroleassignments': {
            'Meta': {'object_name': 'MdlRoleAssignments', 'db_table': "u'mdl_role_assignments'", 'managed': 'False'},
            'contextid': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roleid': ('django.db.models.fields.BigIntegerField', [], {}),
            'userid': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'excercise.mdluser': {
            'Meta': {'object_name': 'MdlUser', 'db_table': "u'mdl_user'", 'managed': 'False'},
            'confirmed': ('django.db.models.fields.IntegerField', [], {}),
            'deleted': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idnumber': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'suspended': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'excercise.mdluserenrolments': {
            'Meta': {'object_name': 'MdlUserEnrolments', 'db_table': "u'mdl_user_enrolments'", 'managed': 'False'},
            'enrolid': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.BigIntegerField', [], {}),
            'userid': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'excercise.question': {
            'Meta': {'object_name': 'Question'},
            'answer_type': ('django.db.models.fields.CharField', [], {'default': "u'T'", 'max_length': '1'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'suggested_answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'excercise.submission': {
            'Meta': {'object_name': 'Submission'},
            'datetime_corrected': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'datetime_submitted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'examiner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'submission_examiner'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['excercise.Exercise']"}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "u'I'", 'max_length': '1'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['excercise']