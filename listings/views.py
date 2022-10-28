from django.shortcuts import render, get_object_or_404
from .models import Listing
# Create your views here.

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings':listings})

def listing(request, id):
    listing = get_object_or_404(Listing, pk=id)
    return render(request, 'listing.html', {'listing':listing})

