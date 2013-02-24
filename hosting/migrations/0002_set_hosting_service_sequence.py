# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        db.execute(
            'ALTER SEQUENCE hosting_djangohostingservice_id_seq RESTART WITH 10000')

    def backwards(self, orm):
        db.execute(
            'ALTER SEQUENCE hosting_djangohostingservice_id_seq RESTART WITH 1')

    complete_apps = ['hosting']
