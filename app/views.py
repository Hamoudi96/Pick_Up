from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render
import googlemaps


def index(request):
    return render(request, 'index.html')


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def location(request):
    gmaps = googlemaps.Client(key='AIzaSyCKPH1UUPYRIaQ71Ep-8urwmBNKlSIBdHw')
    location1 = '1600 Amphitheatre Parkway, Mountain View, CA'
    location2 = '3 Prarie View Ct, Durham, NC'
    return JsonResponse(pullDistanceFrom(gmaps.distance_matrix(location1,location2)), safe=False)

def pullDistanceFrom(gmapsResult):
    return {"meterDist" : gmapsResult["rows"][0]["elements"][0]["distance"]["value"]}

