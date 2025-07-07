from .views import ProfileUpdateView
from django.urls import path
urlpatterns = [path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit")]
