from django.db import models

# Create your models here.
class Location(models.Model):
    prenom = models.TextField()
    nom = models.TextField()
    telephone = models.TextField()
    nationalite = models.TextField()
    date_arrivee = models.DateField()
    date_depart = models.DateField()
    loyer = models.DecimalField(max_digits=11, decimal_places=2)
    commentaires = models.TextField()

    class Meta:
        ordering = ["date_arrivee"]


class Params(models.Model):
    lien = models.BooleanField()
    numero = models.TextField()
    loyer = models.DecimalField(max_digits=11, decimal_places=2)