from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'pages_app_templates/index.html')


def about(request):
    return render(request, 'pages_app_templates/about.html')
