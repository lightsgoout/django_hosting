# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'DjangoHostingTariff'
        db.create_table(u'hosting_djangohostingtariff', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True,
                                                                  max_length=255)),
            ('is_published',
             self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'hosting', ['DjangoHostingTariff'])

        # Adding model 'DjangoHostingAccount'
        db.create_table(u'hosting_djangohostingaccount', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='hosting_accounts', on_delete=models.PROTECT,
                to=orm['accounts.Client'])),
            ('tariff', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['hosting.DjangoHostingTariff'],
                on_delete=models.PROTECT)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')(
                auto_now_add=True, blank=True)),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'hosting', ['DjangoHostingAccount'])

        # Adding model 'DjangoHostingService'
        db.create_table(u'hosting_djangohostingservice', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='hosting_services',
                to=orm['hosting.DjangoHostingAccount'])),
            ('python_version',
             self.gf('django.db.models.fields.related.ForeignKey')(
                 to=orm['backend.PythonVersion'], on_delete=models.PROTECT)),
            ('django_version',
             self.gf('django.db.models.fields.related.ForeignKey')(
                 to=orm['backend.DjangoVersion'], on_delete=models.PROTECT)),
            ('virtualenv_path',
             self.gf('django.db.models.fields.CharField')(unique=True,
                                                          max_length=255)),
            ('home_path',
             self.gf('django.db.models.fields.CharField')(unique=True,
                                                          max_length=255)),
            ('server', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['backend.DjangoHostingServer'],
                on_delete=models.PROTECT)),
            ('status',
             self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'hosting', ['DjangoHostingService'])


    def backwards(self, orm):
        # Deleting model 'DjangoHostingTariff'
        db.delete_table(u'hosting_djangohostingtariff')

        # Deleting model 'DjangoHostingAccount'
        db.delete_table(u'hosting_djangohostingaccount')

        # Deleting model 'DjangoHostingService'
        db.delete_table(u'hosting_djangohostingservice')


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
        }
    }

    complete_apps = ['hosting']
