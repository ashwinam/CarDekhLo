from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_listing, name='create'),
    path('listing/', views.listings, name='listings'),
    path('update/<int:id>', views.update_listing, name='update'),
    path('listing/<int:id>', views.listing, name='listing'),
]
