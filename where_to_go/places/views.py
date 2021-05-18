

from django.shortcuts import render

from .models import Place


def places(request):
    places = Place.objects.all().fetch_places_geojson()
    return render(request, "index.html", context={'places': places})
