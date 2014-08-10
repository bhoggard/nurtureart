# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artwork'
        db.create_table(u'benefit_artwork', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('artist_first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('artist_last_name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('addresss', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('work_year', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('medium', self.gf('django.db.models.fields.TextField')()),
            ('edition', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'benefit', ['Artwork'])


    def backwards(self, orm):
        # Deleting model 'Artwork'
        db.delete_table(u'benefit_artwork')


    models = {
        u'benefit.artwork': {
            'Meta': {'ordering': "('artist_last_name', 'artist_first_name', 'title')", 'object_name': 'Artwork'},
            'addresss': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'artist_first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'artist_last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.TextField', [], {}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'work_year': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['benefit']