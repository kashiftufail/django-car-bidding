from django.urls import path
from .views import place_or_update_bid

app_name = "bidding"

urlpatterns = [
    path('place/<int:car_id>/', place_or_update_bid, name='place_or_update_bid'),
]