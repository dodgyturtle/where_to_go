from django.contrib import admin
from django.shortcuts import get_object_or_404

from .handlers import generate_place_details, write_details_to_json
from .models import Place, PlaceImage


class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("place_title",)}


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)
