from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from .models import Artwork, Page
from django.views.generic import DetailView, ListView

def index(request):
    page = Page.objects.get(title='Home')
    context = {
        'body': page.body_as_html(),
    }
    return render(request, 'index.html', context)

class ArtworkList(ListView):
  queryset = Artwork.objects.order_by('artist_last_name', 'artist_first_name', 'title')
  template_name = "artwork_list.html"
  context_object_name = "artwork_list"
  paginate_by = 18

artwork_list = ArtworkList.as_view()

def artwork_detail(request, artwork_id):
    context = {}
    try:
        artwork = Artwork.objects.get(pk=artwork_id)
        context['artwork'] = artwork
        ids = Artwork.objects.order_by('artist_last_name', 'artist_first_name', 'title', 'id').values_list('id', flat=True)
        index = list(ids).index(artwork.pk)
        if index > 0:
            context['prev'] = ids[index - 1]
        if index < len(ids) - 1:
            context['next'] = ids[index + 1]
    except Artwork.DoesNotExist:
        raise Http404
    return render_to_response('benefit/artwork_detail.html', context)
