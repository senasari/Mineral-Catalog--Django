from django.http import HttpResponse
from django.shortcuts import render


def index_page(request):
    """Renders an index page to welcome users"""
    return render(request, 'home.html')
