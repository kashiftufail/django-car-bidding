# cars/urls.py
from django.urls import path
from .views import (
    CarListView,
    CarCreateView,
    CarDetailView,
    CarUpdateView,
    CarDeleteView,
)

app_name = 'cars'

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('new/', CarCreateView.as_view(), name='car_create'),
    path('<slug:slug>/', CarDetailView.as_view(), name='car_detail'),
    path('<slug:slug>/edit/', CarUpdateView.as_view(), name='car_update'),
    path('<slug:slug>/delete/', CarDeleteView.as_view(), name='car_delete'),
]