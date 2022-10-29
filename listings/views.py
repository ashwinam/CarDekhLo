from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .forms import ListingForm
# Create your views here.

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings':listings})

def listing(request, id):
    listing = get_object_or_404(Listing, pk=id)
    return render(request, 'listing.html', {'listing':listing})

def create_listing(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect ('/listing/')
    return render(request, 'create.html', {'form':form})

def update_listing(request, id):
    listing = get_object_or_404(Listing, pk=id)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid:
            form.save()
            return redirect('/listing/')
    return render(request, 'create.html', {"form":form})

