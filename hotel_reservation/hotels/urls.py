from django.urls import path
from .views import hotel_list

urlpatterns = [
    path('api/hotels/', hotel_list, name='hotel-list'),
]
