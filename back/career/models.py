from django.db import models

# Create your models here.


class Offre(models.Model):
    intitule = models.TextField()
    type = models.TextField()
    entreprise = models.TextField()
    adresse = models.TextField()
    etat = models.TextField()
    url = models.TextField()

    class Meta:
        ordering = ["id"]
