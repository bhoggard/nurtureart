from django.shortcuts import render
from benefit.models import Page

def index(request):
    page = Page.objects.get(title='Home')
    context = {
        'body': page.body_as_html(),
    }
    return render(request, 'index.html', context)