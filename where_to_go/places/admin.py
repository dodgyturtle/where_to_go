from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ["place_image"]
    def place_image(self, obj):
        return format_html(f'<img src="{obj.image_url.url}" width="200"/>')


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ["place_image"]
    fields = ("image_url", "place_image", "sort_order")

    def place_image(self, obj):
        return format_html(f'<img src="{obj.image_url.url}" width="200"/>')


class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("place_title",)}
    inlines = [
        PlaceImageInline,
    ]
    search_fields = ['place_title']


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)
