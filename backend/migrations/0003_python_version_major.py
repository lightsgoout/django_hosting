# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'PythonVersion.major_version'
        db.add_column(u'backend_pythonversion', 'major_version',
                      self.gf('django.db.models.fields.CharField')(
                          default='python2.7', max_length=15),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PythonVersion.major_version'
        db.delete_column(u'backend_pythonversion', 'major_version')


    models = {
        u'backend.djangohostingserver': {
            'Meta': {'object_name': 'DjangoHostingServer'},
            'core_count': (
            'django.db.models.fields.PositiveSmallIntegerField', [],
            {'default': '1'}),
            'hostname': ('django.db.models.fields.CharField', [],
                         {'unique': 'True', 'max_length': '255'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'supported_python_versions': (
            'django.db.models.fields.related.ManyToManyField', [],
            {'to': u"orm['backend.PythonVersion']", 'symmetrical': 'False'})
        },
        u'backend.djangoversion': {
            'Meta': {'object_name': 'DjangoVersion'},
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_discontinued': (
            'django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_stable': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'supported_python_versions': (
            'django.db.models.fields.related.ManyToManyField', [],
            {'to': u"orm['backend.PythonVersion']", 'symmetrical': 'False'}),
            'version_family': ('django.db.models.fields.CharField', [],
                               {'unique': 'True', 'max_length': '15'})
        },
        u'backend.pythonversion': {
            'Meta': {'object_name': 'PythonVersion'},
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_discontinued': (
            'django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_stable': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'major_version': (
            'django.db.models.fields.CharField', [], {'max_length': '15'}),
            'version_family': ('django.db.models.fields.CharField', [],
                               {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['backend']
