from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .handlers import generate_place_details
from .models import Place


def places(request):
    places = Place.objects.all().fetch_places_geojson()
    return render(request, "index.html", context={"places": places})


def place_details_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = generate_place_details(place)
    return JsonResponse(
        place_details,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )
