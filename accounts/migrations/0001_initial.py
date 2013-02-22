# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'BillingInformation'
        db.create_table(u'accounts_billinginformation', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='billing_information', to=orm['auth.User'])),
            ('country',
             self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('city',
             self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('address',
             self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zip_code',
             self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('phone',
             self.gf('django.db.models.fields.CharField')(max_length=31)),
        ))
        db.send_create_signal(u'accounts', ['BillingInformation'])


    def backwards(self, orm):
        # Deleting model 'BillingInformation'
        db.delete_table(u'accounts_billinginformation')


    models = {
        u'accounts.billinginformation': {
            'Meta': {'object_name': 'BillingInformation'},
            'address': (
            'django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': (
            'django.db.models.fields.CharField', [], {'max_length': '127'}),
            'client': ('django.db.models.fields.related.ForeignKey', [],
                       {'related_name': "'billing_information'",
                        'to': u"orm['auth.User']"}),
            'country': (
            'django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': (
            'django.db.models.fields.CharField', [], {'max_length': '31'}),
            'zip_code': (
            'django.db.models.fields.CharField', [], {'max_length': '63'})
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
        }
    }

    complete_apps = ['accounts']
