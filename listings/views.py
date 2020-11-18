from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'listings/listings.html')


# Create your views here.
def listing(request):
    return render(request, 'listings/listing_single.html')


# Create your views here.
def search(request):
    return render(request, 'listings/search.html')
