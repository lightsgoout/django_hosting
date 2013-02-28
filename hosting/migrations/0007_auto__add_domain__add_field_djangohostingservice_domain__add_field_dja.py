# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Domain'
        db.create_table(u'hosting_domain', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain',
             self.gf('django.db.models.fields.CharField')(unique=True,
                                                          max_length=255)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='domains', on_delete=models.PROTECT,
                to=orm['auth.User'])),
        ))
        db.send_create_signal(u'hosting', ['Domain'])

        # Adding field 'DjangoHostingService.domain'
        db.add_column(u'hosting_djangohostingservice', 'domain',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          default=0, to=orm['hosting.Domain'],
                          on_delete=models.PROTECT),
                      keep_default=False)

        # Adding field 'DjangoHostingService.django_static_path'
        db.add_column(u'hosting_djangohostingservice', 'django_static_path',
                      self.gf('django.db.models.fields.CharField')(
                          default='static', max_length=255, null=True,
                          blank=True),
                      keep_default=False)

        # Adding field 'DjangoHostingService.django_static_url'
        db.add_column(u'hosting_djangohostingservice', 'django_static_url',
                      self.gf('django.db.models.fields.CharField')(
                          default='/static/', max_length=255, null=True,
                          blank=True),
                      keep_default=False)

        # Adding field 'DjangoHostingService.django_media_path'
        db.add_column(u'hosting_djangohostingservice', 'django_media_path',
                      self.gf('django.db.models.fields.CharField')(
                          default='media', max_length=255, null=True,
                          blank=True),
                      keep_default=False)

        # Adding field 'DjangoHostingService.django_media_url'
        db.add_column(u'hosting_djangohostingservice', 'django_media_url',
                      self.gf('django.db.models.fields.CharField')(
                          default='/media/', max_length=255, null=True,
                          blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Domain'
        db.delete_table(u'hosting_domain')

        # Deleting field 'DjangoHostingService.domain'
        db.delete_column(u'hosting_djangohostingservice', 'domain_id')

        # Deleting field 'DjangoHostingService.django_static_path'
        db.delete_column(u'hosting_djangohostingservice', 'django_static_path')

        # Deleting field 'DjangoHostingService.django_static_url'
        db.delete_column(u'hosting_djangohostingservice', 'django_static_url')

        # Deleting field 'DjangoHostingService.django_media_path'
        db.delete_column(u'hosting_djangohostingservice', 'django_media_path')

        # Deleting field 'DjangoHostingService.django_media_url'
        db.delete_column(u'hosting_djangohostingservice', 'django_media_url')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '80'}),
            'permissions': (
            'django.db.models.fields.related.ManyToManyField', [],
            {'to': u"orm['auth.Permission']", 'symmetrical': 'False',
             'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {
            'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')",
            'unique_together': "((u'content_type', u'codename'),)",
            'object_name': 'Permission'},
            'codename': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [],
                             {'to': u"orm['contenttypes.ContentType']"}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': (
            'django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [],
                            {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [],
                      {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [],
                           {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'to': u"orm['auth.Group']", 'symmetrical': 'False',
                        'blank': 'True'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': (
            'django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': (
            'django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [],
                           {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [],
                          {'max_length': '30', 'blank': 'True'}),
            'password': (
            'django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': (
            'django.db.models.fields.related.ManyToManyField', [],
            {'to': u"orm['auth.Permission']", 'symmetrical': 'False',
             'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [],
                         {'unique': 'True', 'max_length': '30'})
        },
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
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)",
                     'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType',
                     'db_table': "'django_content_type'"},
            'app_label': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': (
            'django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': (
            'django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hosting.djangohostingaccount': {
            'Meta': {'object_name': 'DjangoHostingAccount'},
            'client': ('django.db.models.fields.related.ForeignKey', [],
                       {'related_name': "'hosting_accounts'",
                        'on_delete': 'models.PROTECT',
                        'to': u"orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [],
                           {'auto_now_add': 'True', 'blank': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [],
                       {'default': "'T'", 'max_length': '1'}),
            'tariff': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['hosting.DjangoHostingTariff']",
                        'on_delete': 'models.PROTECT'})
        },
        u'hosting.djangohostingservice': {
            'Meta': {'object_name': 'DjangoHostingService'},
            'account': ('django.db.models.fields.related.ForeignKey', [],
                        {'related_name': "'hosting_services'",
                         'to': u"orm['hosting.DjangoHostingAccount']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [],
                           {'auto_now_add': 'True', 'blank': 'True'}),
            'django_media_path': ('django.db.models.fields.CharField', [],
                                  {'default': "'media'", 'max_length': '255',
                                   'null': 'True', 'blank': 'True'}),
            'django_media_url': ('django.db.models.fields.CharField', [],
                                 {'default': "'/media/'", 'max_length': '255',
                                  'null': 'True', 'blank': 'True'}),
            'django_static_path': ('django.db.models.fields.CharField', [],
                                   {'default': "'static'", 'max_length': '255',
                                    'null': 'True', 'blank': 'True'}),
            'django_static_url': ('django.db.models.fields.CharField', [],
                                  {'default': "'/static/'",
                                   'max_length': '255', 'null': 'True',
                                   'blank': 'True'}),
            'django_version': (
            'django.db.models.fields.related.ForeignKey', [],
            {'to': u"orm['backend.DjangoVersion']",
             'on_delete': 'models.PROTECT'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['hosting.Domain']",
                        'on_delete': 'models.PROTECT'}),
            'home_path': ('django.db.models.fields.CharField', [],
                          {'max_length': '255', 'unique': 'True',
                           'null': 'True', 'blank': 'True'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'python_version': (
            'django.db.models.fields.related.ForeignKey', [],
            {'to': u"orm['backend.PythonVersion']",
             'on_delete': 'models.PROTECT'}),
            'server': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['backend.DjangoHostingServer']",
                        'on_delete': 'models.PROTECT'}),
            'status': ('django.db.models.fields.CharField', [],
                       {'default': "'D'", 'max_length': '1'}),
            'virtualenv_path': ('django.db.models.fields.CharField', [],
                                {'max_length': '255', 'unique': 'True',
                                 'null': 'True', 'blank': 'True'})
        },
        u'hosting.djangohostingtariff': {
            'Meta': {'object_name': 'DjangoHostingTariff'},
            'cpu_per_process': (
            'django.db.models.fields.IntegerField', [], {}),
            'disk_quota': ('django.db.models.fields.IntegerField', [], {}),
            'file_descriptors_per_process': (
            'django.db.models.fields.IntegerField', [], {}),
            'has_backup': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inode_quota': ('django.db.models.fields.BigIntegerField', [], {}),
            'is_published': (
            'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [],
                     {'unique': 'True', 'max_length': '255'}),
            'ram_per_process': (
            'django.db.models.fields.IntegerField', [], {}),
            'vhost_count': (
            'django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'workers_per_host': (
            'django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'hosting.domain': {
            'Meta': {'object_name': 'Domain'},
            'domain': ('django.db.models.fields.CharField', [],
                       {'unique': 'True', 'max_length': '255'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [],
                      {'related_name': "'domains'",
                       'on_delete': 'models.PROTECT',
                       'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['hosting']
