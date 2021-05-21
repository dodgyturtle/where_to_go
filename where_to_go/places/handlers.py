import json

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage


def generate_place_details(place):
    place_details = {
        "title": place.place_title,
        "imgs": [image.image_url.url for image in place.place_images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.longitude, "lat": place.latitude},
    }
    return place_details
