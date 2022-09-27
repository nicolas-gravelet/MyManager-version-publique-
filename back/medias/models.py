from django.db import models

# Create your models here.


class Media(models.Model):
    titre = models.TextField()
    type = models.TextField()
    genre = models.TextField()
    studios = models.TextField()
    support = models.TextField()
    annee = models.IntegerField()
    etat = models.TextField()

    class Meta:
        ordering = ["id"]
