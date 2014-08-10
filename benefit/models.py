from django.db import models

# Create your models here.

class Artwork(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    artist_first_name = models.CharField(max_length=255, blank=True)
    artist_last_name = models.CharField(max_length=255,db_index=True)
    website = models.URLField(blank=True)
    addresss = models.TextField(blank=True)
    email = models.EmailField(max_length=255)
    work_year = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    medium = models.TextField()
    edition = models.CharField(max_length=255,blank=True,help_text="leave blank if not editioned")
    image = models.ImageField(upload_to='images',null=True)

    def image_tag(self):
        return u'<img src="%s" />' % self.image.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['artist_last_name',]
