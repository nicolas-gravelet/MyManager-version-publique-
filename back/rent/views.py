from django.shortcuts import render
from rest_framework import viewsets
from rent.models import Location, Params
from rent.serializers import LocationSerializer, ParamsSerializer

# Create your views here.

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ParamsViewSet(viewsets.ModelViewSet):
    queryset = Params.objects.all()
    serializer_class = ParamsSerializer
    