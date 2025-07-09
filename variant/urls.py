from django.urls import path
from . import views

urlpatterns = [
    path("by-make/", views.variant_list_by_make, name="variant_by_make"),
]