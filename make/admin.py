from django.contrib import admin
from .models import Make

@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)