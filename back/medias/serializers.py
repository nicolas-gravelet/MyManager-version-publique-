from rest_framework import serializers

from medias.models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["id", "titre", "type", "genre",
                  "studios", "support", "annee", "etat"]
