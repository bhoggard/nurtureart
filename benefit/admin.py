from django.contrib import admin
from .models import Artwork

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_first_name', 'artist_last_name')
    search_fields = ['title', 'artist_first_name', 'artist_last_name']

admin.site.register(Artwork, ArtworkAdmin)

