from django.shortcuts import render
from .models import Listing
# Create your views here.

def listings(request):
    listing = Listing.objects.all()
    return render(request, 'listings.html', {'listings':listing})

