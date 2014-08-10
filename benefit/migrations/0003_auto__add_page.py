# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'benefit_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'benefit', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'benefit_page')


    models = {
        u'benefit.artwork': {
            'Meta': {'ordering': "['artist_last_name']", 'object_name': 'Artwork'},
            'addresss': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'artist_first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'artist_last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'medium': ('django.db.models.fields.TextField', [], {}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'work_year': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'benefit.page': {
            'Meta': {'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['benefit']