from django.shortcuts import render


def hello_world(request):
    render(request, 'index.html')
