from django.shortcuts import render
from breadcrumbs.models import Node

# Create your views here.


def show_nodes(request):
    html = 'index.html'
    context = {
        'node': Node.objects.all()
    }
    return render(request, html, context)