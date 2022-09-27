from dataclasses import fields
from rest_framework import serializers
from career.models import Offre


class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = ["id", "intitule", "type",
                  "entreprise", "adresse", "etat", "url"]
