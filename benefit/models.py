from django.db import models
from django.utils.html import format_html
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

class Artwork(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    artist_first_name = models.CharField(max_length=255, blank=True)
    artist_last_name = models.CharField(max_length=255,db_index=True)
    website = models.URLField(blank=True)
    addresss = models.TextField(blank=True)
    email = models.EmailField(max_length=255,blank=True)
    work_year = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    medium = models.TextField()
    edition = models.CharField(max_length=255,blank=True,help_text="leave blank if not editioned")
    image = models.ImageField(upload_to='images',null=True)
    image_large = ImageSpecField(source='image',
                                     processors=[ResizeToFit(800, 800, False)],
                                     format='JPEG',
                                     options={'quality': 100})
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(140, 140)],
                                     format='JPEG',
                                     options={'quality': 60})

    image_tiny = ImageSpecField(source='image',
                                processors=[ResizeToFill(80, 80)],
                                format='JPEG',
                                options={'quality': 60})

    def image_tag(self):
        return u'<img src="%s" />' % self.image_large.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def thumbnail_tag(self):
        return u'<img src="%s" />' % self.image_thumbnail.url

    thumbnail_tag.short_description = 'Thumbnail'
    thumbnail_tag.allow_tags = True

    def tiny_tag(self):
        return u'<img src="%s" />' % self.image_tiny.url

    tiny_tag.short_description = 'Thumbnail'
    tiny_tag.allow_tags = True

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['artist_last_name',]

class Page(models.Model):
    title = models.CharField(max_length=255,unique=True)
    body = models.TextField()

    def body_as_html(self):
        return format_html(self.body)

    def __unicode__(self):
        return self.title
