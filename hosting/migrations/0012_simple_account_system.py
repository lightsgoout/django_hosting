# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting model 'DjangoHostingAccount'
        db.delete_table(u'hosting_djangohostingaccount')

        # Deleting field 'DjangoHostingService.account'
        db.delete_column(u'hosting_djangohostingservice', 'account_id')

        # Adding field 'DjangoHostingService.owner'
        db.add_column(u'hosting_djangohostingservice', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          related_name='django_services',
                          on_delete=models.PROTECT, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'DjangoHostingService.tariff'
        db.add_column(u'hosting_djangohostingservice', 'tariff',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          to=orm['hosting.DjangoHostingTariff'],
                          on_delete=models.PROTECT),
                      keep_default=False)

        # Adding field 'DjangoHostingService.start_at'
        db.add_column(u'hosting_djangohostingservice', 'start_at',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Adding field 'DjangoHostingService.end_at'
        db.add_column(u'hosting_djangohostingservice', 'end_at',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'DjangoHostingAccount'
        db.create_table(u'hosting_djangohostingaccount', (
            ('status',
             self.gf('django.db.models.fields.CharField')(default='T',
                                                          max_length=1)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(
                auto_now_add=True, blank=True)),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('tariff', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['hosting.DjangoHostingTariff'],
                on_delete=models.PROTECT)),
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='hosting_accounts', on_delete=models.PROTECT,
                to=orm['auth.User'])),
        ))
        db.send_create_signal(u'hosting', ['DjangoHostingAccount'])


        # User chose to not deal with backwards NULL issues for 'DjangoHostingService.account'
        raise RuntimeError(
            "Cannot reverse this migration. 'DjangoHostingService.account' and its values cannot be restored.")
        # Deleting field 'DjangoHostingService.owner'
        db.delete_column(u'hosting_djangohostingservice', 'owner_id')

        # Deleting field 'DjangoHostingService.tariff'
        db.delete_column(u'hosting_djangohostingservice', 'tariff_id')

        # Deleting field 'DjangoHostingService.start_at'
        db.delete_column(u'hosting_djangohostingservice', 'start_at')

        # Deleting field 'DjangoHostingService.end_at'
        db.delete_column(u'hosting_djangohostingservice', 'end_at')


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
        u'hosting.djangohostingservice': {
            'Meta': {'object_name': 'DjangoHostingService'},
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
            'end_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [],
                      {'related_name': "'django_services'",
                       'on_delete': 'models.PROTECT',
                       'to': u"orm['auth.User']"}),
            'python_version': (
            'django.db.models.fields.related.ForeignKey', [],
            {'to': u"orm['backend.PythonVersion']",
             'on_delete': 'models.PROTECT'}),
            'requirements_file': ('django.db.models.fields.CharField', [],
                                  {'max_length': '255', 'null': 'True',
                                   'blank': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['backend.DjangoHostingServer']",
                        'on_delete': 'models.PROTECT'}),
            'settings_module': ('django.db.models.fields.CharField', [],
                                {'default': "'settings'",
                                 'max_length': '255'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [],
                       {'default': "'D'", 'max_length': '1'}),
            'tariff': ('django.db.models.fields.related.ForeignKey', [],
                       {'to': u"orm['hosting.DjangoHostingTariff']",
                        'on_delete': 'models.PROTECT'}),
            'wsgi_module': ('django.db.models.fields.CharField', [],
                            {'max_length': '255', 'null': 'True',
                             'blank': 'True'})
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
