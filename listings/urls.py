from django.urls import path
from . import views

urlpatterns = [
    path('listing/', views.listings, name='listings'),
    path('listing/<int:id>', views.listing, name='listing'),
]
