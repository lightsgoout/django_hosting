# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'PythonVersion'
        db.create_table(u'backend_pythonversion', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version_family',
             self.gf('django.db.models.fields.CharField')(unique=True,
                                                          max_length=15)),
            ('is_stable',
             self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_discontinued',
             self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_published',
             self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'backend', ['PythonVersion'])

        # Adding model 'DjangoVersion'
        db.create_table(u'backend_djangoversion', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version_family',
             self.gf('django.db.models.fields.CharField')(unique=True,
                                                          max_length=15)),
            ('is_stable',
             self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_discontinued',
             self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_published',
             self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'backend', ['DjangoVersion'])

        # Adding M2M table for field supported_python_versions on 'DjangoVersion'
        db.create_table(u'backend_djangoversion_supported_python_versions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True,
                                    auto_created=True)),
            ('djangoversion',
             models.ForeignKey(orm[u'backend.djangoversion'], null=False)),
            ('pythonversion',
             models.ForeignKey(orm[u'backend.pythonversion'], null=False))
        ))
        db.create_unique(u'backend_djangoversion_supported_python_versions',
                         ['djangoversion_id', 'pythonversion_id'])

        # Adding model 'DjangoHostingServer'
        db.create_table(u'backend_djangohostingserver', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname',
             self.gf('django.db.models.fields.CharField')(unique=True,
                                                          max_length=255)),
            ('is_published',
             self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'backend', ['DjangoHostingServer'])

        # Adding M2M table for field supported_python_versions on 'DjangoHostingServer'
        db.create_table(
            u'backend_djangohostingserver_supported_python_versions', (
                ('id', models.AutoField(verbose_name='ID', primary_key=True,
                                        auto_created=True)),
                ('djangohostingserver',
                 models.ForeignKey(orm[u'backend.djangohostingserver'],
                                   null=False)),
                ('pythonversion',
                 models.ForeignKey(orm[u'backend.pythonversion'], null=False))
            ))
        db.create_unique(
            u'backend_djangohostingserver_supported_python_versions',
            ['djangohostingserver_id', 'pythonversion_id'])


    def backwards(self, orm):
        # Deleting model 'PythonVersion'
        db.delete_table(u'backend_pythonversion')

        # Deleting model 'DjangoVersion'
        db.delete_table(u'backend_djangoversion')

        # Removing M2M table for field supported_python_versions on 'DjangoVersion'
        db.delete_table('backend_djangoversion_supported_python_versions')

        # Deleting model 'DjangoHostingServer'
        db.delete_table(u'backend_djangohostingserver')

        # Removing M2M table for field supported_python_versions on 'DjangoHostingServer'
        db.delete_table(
            'backend_djangohostingserver_supported_python_versions')


    models = {
        u'backend.djangohostingserver': {
            'Meta': {'object_name': 'DjangoHostingServer'},
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
            'version_family': ('django.db.models.fields.CharField', [],
                               {'unique': 'True', 'max_length': '15'})
        }
    }

    complete_apps = ['backend']
