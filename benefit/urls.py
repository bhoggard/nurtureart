from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, TemplateView
from .models import Artwork
from .views import ArtworkList

urlpatterns = patterns('',
    url(r'^$', 'benefit.views.index', name='index'),
    url(r'^artworks$', 'benefit.views.artwork_list', name='artworks-list'),
    url(r'^artworks/(?P<artwork_id>\d+)$', 'benefit.views.artwork_detail', name='artwork-detail'),
)