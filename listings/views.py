from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import ListingModel
# Create your views here.


def index(request):
    listings = ListingModel.objects.order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings': page_listings
    }

    return render(request, 'listings/listings.html', context)


# Create your views here.
def listing(request, listing_id):
    return render(request, 'listings/listing_single.html')


# Create your views here.
def search(request):
    return render(request, 'listings/search.html')
