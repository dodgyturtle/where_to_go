import os

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def fetch_response(link: str, params: dict = {}) -> requests.models.Response:
    link_response = requests.get(link, verify=False, params=params)
    link_response.raise_for_status()
    return link_response


class Command(BaseCommand):
    help = "Command for download from URL(JSON) informations about interesting place."

    def add_arguments(self, parser):
        parser.add_argument(
            "url", nargs=1, type=str, help="Адрес на JSON файл с описанием места"
        )

    def handle(self, *args, **options):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        for url in options["url"]:
            try:
                link_response = fetch_response(url)
                place_json_description = link_response.json()
                place, place_created = Place.objects.get_or_create(
                    place_title=place_json_description["title"],
                    description_short=place_json_description["description_short"],
                    description_long=place_json_description["description_long"],
                    latitude=place_json_description["coordinates"]["lat"],
                    longitude=place_json_description["coordinates"]["lng"],
                )
                if place_created:
                    for index, image_url in enumerate(place_json_description["imgs"]):
                        image_filename = os.path.basename(image_url)
                        response = fetch_response(image_url)
                        image, image_created = PlaceImage.objects.get_or_create(
                            sort_order=index,
                            place=place,
                        )
                        image.image_url.save(
                            image_filename, ContentFile(response.content), save=True
                        )
                if place_created and image_created:
                    print(f"Данные по месту { place } записаны в базу")
            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
            ) as error:
                print(f"Произошла ошибка: { error }")
