from django.contrib import admin
from django.shortcuts import get_object_or_404

from .handlers import generate_place_details, write_details_to_json
from .models import Place, PlaceImage


class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("place_title",)}

    def response_change(self, request, obj):
        response = super().response_change(request, obj)
        place_details = generate_place_details(obj)
        json_filename = f"{obj.slug}.json"
        write_details_to_json(place_details, json_filename)
        return response

    def response_add(self, request, obj, post_url_continue=None):
        response = super().response_add(request, obj, post_url_continue=None)
        place_details = generate_place_details(obj)
        json_filename = f"{obj.slug}.json"
        write_details_to_json(place_details, json_filename)
        return response


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)
