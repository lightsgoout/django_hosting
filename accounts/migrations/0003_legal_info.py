# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'DjangoAccount.company_name'
        db.add_column(u'accounts_djangoaccount', 'company_name',
                      self.gf('django.db.models.fields.CharField')(
                          max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DjangoAccount.legal_type'
        db.add_column(u'accounts_djangoaccount', 'legal_type',
                      self.gf('django.db.models.fields.CharField')(
                          default='person', max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DjangoAccount.company_name'
        db.delete_column(u'accounts_djangoaccount', 'company_name')

        # Deleting field 'DjangoAccount.legal_type'
        db.delete_column(u'accounts_djangoaccount', 'legal_type')


    models = {
        u'accounts.billinginformation': {
            'Meta': {'object_name': 'BillingInformation'},
            'address': (
            'django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': (
            'django.db.models.fields.CharField', [], {'max_length': '127'}),
            'country': (
            'django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': (
            'django.db.models.fields.CharField', [], {'max_length': '31'}),
            'user': ('django.db.models.fields.related.OneToOneField', [],
                     {'related_name': "'billing_information'",
                      'unique': 'True', 'to': u"orm['auth.User']"}),
            'zip_code': (
            'django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        u'accounts.djangoaccount': {
            'Meta': {'object_name': 'DjangoAccount'},
            'company_name': ('django.db.models.fields.CharField', [],
                             {'max_length': '255', 'null': 'True',
                              'blank': 'True'}),
            'django_tariff': ('django.db.models.fields.related.ForeignKey', [],
                              {'to': u"orm['hosting.DjangoHostingTariff']",
                               'null': 'True'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_type': ('django.db.models.fields.CharField', [],
                           {'default': "'person'", 'max_length': '8'}),
            'user': ('django.db.models.fields.related.OneToOneField', [],
                     {'related_name': "'django_account'", 'unique': 'True',
                      'to': u"orm['auth.User']"})
        },
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
        }
    }

    complete_apps = ['accounts']
