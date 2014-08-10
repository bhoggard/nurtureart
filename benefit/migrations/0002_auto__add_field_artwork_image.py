# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artwork.image'
        db.add_column(u'benefit_artwork', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artwork.image'
        db.delete_column(u'benefit_artwork', 'image')


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
        }
    }

    complete_apps = ['benefit']