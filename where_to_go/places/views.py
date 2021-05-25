from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import Place


def generate_place_details(place):
    place_details = {
        "title": place.place_title,
        "imgs": [image.image_url.url for image in place.place_images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.longitude, "lat": place.latitude},
    }
    return place_details


def fetch_places_geojson(places):
    geojson = {"type": "FeatureCollection", "features": []}
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude],
            },
            "properties": {
                "title": place.place_title,
                "placeId": place.id,
                "detailsUrl": reverse("place_details", kwargs={"place_id": place.id}),
            },
        }
        geojson["features"].append(feature)
    return geojson


def places(request):
    places = Place.objects.all()
    places_geojson = fetch_places_geojson(places)
    return render(request, "index.html", context={"places": places_geojson})


def place_details_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = generate_place_details(place)
    return JsonResponse(
        place_details,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )
