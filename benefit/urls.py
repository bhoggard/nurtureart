from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, TemplateView
from .models import Artwork

urlpatterns = patterns('',
    url(r'^$', 'benefit.views.index', name='index'),
    url(r'^artworks$', ListView.as_view(
        model=Artwork, paginate_by=24),
        name='artworks-list'),
    url(r'^artworks/(?P<pk>\d+)$', DetailView.as_view(model=Artwork), name='artwork-detail'),
)