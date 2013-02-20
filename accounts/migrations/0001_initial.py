# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'accounts_client', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password',
             self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(
                default=datetime.datetime.now)),
            ('is_organization',
             self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('full_name',
             self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email',
             self.gf('django.db.models.fields.EmailField')(unique=True,
                                                           max_length=75,
                                                           db_index=True)),
            ('is_active',
             self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'accounts', ['Client'])

        # Adding model 'BillingInformation'
        db.create_table(u'accounts_billinginformation', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='billing_information',
                to=orm['accounts.Client'])),
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
        # Deleting model 'Client'
        db.delete_table(u'accounts_client')

        # Deleting model 'BillingInformation'
        db.delete_table(u'accounts_billinginformation')


    models = {
        u'accounts.billinginformation': {
            'Meta': {'object_name': 'BillingInformation'},
            'address': (
                'django.db.models.fields.CharField', [],
                {'max_length': '255'}),
            'city': (
                'django.db.models.fields.CharField', [],
                {'max_length': '127'}),
            'client': ('django.db.models.fields.related.ForeignKey', [],
                       {'related_name': "'billing_information'",
                        'to': u"orm['accounts.Client']"}),
            'country': (
                'django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True'}),
            'phone': (
                'django.db.models.fields.CharField', [], {'max_length': '31'}),
            'zip_code': (
                'django.db.models.fields.CharField', [], {'max_length': '63'})
        },
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
        }
    }

    complete_apps = ['accounts']
