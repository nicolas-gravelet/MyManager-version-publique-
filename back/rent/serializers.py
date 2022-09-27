from rest_framework import serializers
from rent.models import Location, Params

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "prenom", "nom", "telephone", "nationalite", "date_arrivee", "date_depart", "loyer", "commentaires"]

class ParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Params
        fields = ["id", "lien", "numero", "loyer"]