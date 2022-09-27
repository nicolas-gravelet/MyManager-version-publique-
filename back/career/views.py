from django.shortcuts import render
from rest_framework import viewsets
from career.models import Offre
from career.serializers import OffreSerializer

# Create your views here.


class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
