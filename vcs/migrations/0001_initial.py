# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'GithubSettings'
        db.create_table(u'vcs_githubsettings', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hosting',
             self.gf('django.db.models.fields.related.OneToOneField')(
                 related_name='github', unique=True,
                 to=orm['hosting.DjangoHostingService'])),
            ('login', self.gf('django.db.models.fields.CharField')(unique=True,
                                                                   max_length=128)),
            ('password',
             self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True,
                                                                  max_length=511)),
        ))
        db.send_create_signal(u'vcs', ['GithubSettings'])


    def backwards(self, orm):
        # Deleting model 'GithubSettings'
        db.delete_table(u'vcs_githubsettings')


    models = {
        u'accounts.client': {
            'Meta': {'object_name': 'Client'},
            'email': ('django.db.models.fields.EmailField', [],
                      {'unique': 'True', 'max_length': '75',
                       'db_index': 'True'}),
            'full_name': (
                'django.db.models.fields.CharField', [],
                {'max_length': '255'}),
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'is_active': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'True'}),
            'is_organization': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [],
                           {'default': 'datetime.datetime.now'}),
            'password': (
                'django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'backend.djangohostingserver': {
            'Meta': {'object_name': 'DjangoHostingServer'},
            'hostname': ('django.db.models.fields.CharField', [],
                         {'unique': 'True', 'max_length': '255'}),
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'is_published': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'True'}),
            'supported_python_versions': (
                'django.db.models.fields.related.ManyToManyField', [],
                {'to': u"orm['backend.PythonVersion']",
                 'symmetrical': 'False'})
        },
        u'backend.djangoversion': {
            'Meta': {'object_name': 'DjangoVersion'},
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'is_discontinued': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'False'}),
            'is_published': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'True'}),
            'is_stable': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '127'}),
            'supported_python_versions': (
                'django.db.models.fields.related.ManyToManyField', [],
                {'to': u"orm['backend.PythonVersion']",
                 'symmetrical': 'False'}),
            'version_family': ('django.db.models.fields.CharField', [],
                               {'unique': 'True', 'max_length': '15'})
        },
        u'backend.pythonversion': {
            'Meta': {'object_name': 'PythonVersion'},
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'is_discontinued': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'False'}),
            'is_published': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'True'}),
            'is_stable': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '127'}),
            'version_family': ('django.db.models.fields.CharField', [],
                               {'unique': 'True', 'max_length': '15'})
        },
        u'hosting.djangohostingaccount': {
            'Meta': {'object_name': 'DjangoHostingAccount'},
            'client': ('django.db.models.fields.related.ForeignKey', [],
                       {'related_name': "'hosting_accounts'",
                        'on_delete': 'models.PROTECT',
                        'to': u"orm['accounts.Client']"}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'start_at': ('django.db.models.fields.DateTimeField', [],
                         {'auto_now_add': 'True', 'blank': 'True'}),
            'tariff': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['hosting.DjangoHostingTariff']",
                        'on_delete': 'models.PROTECT'})
        },
        u'hosting.djangohostingservice': {
            'Meta': {'object_name': 'DjangoHostingService'},
            'account': ('django.db.models.fields.related.ForeignKey', [],
                        {'related_name': "'hosting_services'",
                         'to': u"orm['hosting.DjangoHostingAccount']"}),
            'django_version': (
                'django.db.models.fields.related.ForeignKey', [],
                {'to': u"orm['backend.DjangoVersion']",
                 'on_delete': 'models.PROTECT'}),
            'home_path': ('django.db.models.fields.CharField', [],
                          {'unique': 'True', 'max_length': '255'}),
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'python_version': (
                'django.db.models.fields.related.ForeignKey', [],
                {'to': u"orm['backend.PythonVersion']",
                 'on_delete': 'models.PROTECT'}),
            'server': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['backend.DjangoHostingServer']",
                        'on_delete': 'models.PROTECT'}),
            'status': (
                'django.db.models.fields.CharField', [], {'max_length': '1'}),
            'virtualenv_path': ('django.db.models.fields.CharField', [],
                                {'unique': 'True', 'max_length': '255'})
        },
        u'hosting.djangohostingtariff': {
            'Meta': {'object_name': 'DjangoHostingTariff'},
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'is_published': (
                'django.db.models.fields.BooleanField', [],
                {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '255'})
        },
        u'vcs.githubsettings': {
            'Meta': {'object_name': 'GithubSettings'},
            'hosting': ('django.db.models.fields.related.OneToOneField', [],
                        {'related_name': "'github'", 'unique': 'True',
                         'to': u"orm['hosting.DjangoHostingService']"}),
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [],
                      {'unique': 'True', 'max_length': '128'}),
            'password': (
                'django.db.models.fields.CharField', [],
                {'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '511'})
        }
    }

    complete_apps = ['vcs']
