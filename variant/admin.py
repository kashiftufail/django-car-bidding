# variant/admin.py

from django.contrib import admin
from .models import Variant

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("name", "make")
    list_filter = ("make",)
    search_fields = ("name", "make__name")
