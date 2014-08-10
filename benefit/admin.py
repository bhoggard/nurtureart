from django.contrib import admin
from .models import Artwork, Page

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_last_name', 'artist_first_name', 'thumbnail_tag')
    search_fields = ['title', 'artist_first_name', 'artist_last_name',]
    readonly_fields = ('image_tag',)

admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Page)

