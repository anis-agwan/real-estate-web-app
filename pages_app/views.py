from django.shortcuts import render
from django.http import HttpResponse

from listings.models import ListingModel
from realtors.models import RealtorModel
# Create your views here.


def index(request):
    listings = ListingModel.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages_app_templates/index.html', context)


def about(request):
    # Get all realtors
    realtors = RealtorModel.objects.order_by(
        '-hire_date')

    # Get MVP
    mvp_realtors = RealtorModel.objects.all().filter(is_MVP=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages_app_templates/about.html', context)
