from django.contrib import admin
from .models import Car
from images.models import Image
from django.utils.safestring import mark_safe

from images.forms import ImageInlineFormSet


class ImageInline(admin.TabularInline):
    model = Image
    formset = ImageInlineFormSet
    fields = ['preview', 'file', 'alt_text', 'uploaded_by']
    readonly_fields = ['preview', 'uploaded_by']
    extra = 1
    can_delete = True

    def preview(self, obj):
        if obj.file:
            return mark_safe(f'<img src="{obj.file.url}" width="100" height="60" style="object-fit:cover;border-radius:4px;" />')
        return "No Image"
    preview.short_description = "Preview"

    def get_formset(self, request, obj=None, **kwargs):
        FormSet = super().get_formset(request, obj, **kwargs)
        class WrappedFormSet(FormSet):
            def __init__(self2, *args, **kwargs):
                kwargs['request'] = request
                super().__init__(*args, **kwargs)
        return WrappedFormSet


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "title", "variant", "seller", "manufacture_year",
        "odometer", "fuel_type", "car_type", "auction_datetime"
    )
    search_fields = ("title", "variant__name", "seller__user__username")
    list_filter = ("fuel_type", "car_type", "manufacture_year", "auction_datetime")

    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "slug", "variant", "color", "seller")
        }),
        ("Specifications", {
            "fields": (
                "manufacture_year", "odometer", "weight",
                "car_type", "fuel_type", "has_keys", "engine_starts"
            )
        }),
        ("Auction & Location", {
            "fields": ("location", "auction_datetime")
        }),
        ("Details", {
            "fields": ("detail",)
        }),
    )

    readonly_fields = ("slug",)
    inlines = [ImageInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
