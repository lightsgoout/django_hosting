# -*- coding: utf-8 -*-
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

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
            'django_version': (
            'django.db.models.fields.related.ForeignKey', [],
            {'to': u"orm['backend.DjangoVersion']",
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
    }

    complete_apps = ['hosting']
