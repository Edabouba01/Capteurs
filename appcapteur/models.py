from django.db import models

from django.db import models

class Mesure(models.Model):
    humidite = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class Temperature(Mesure):
    nom_capteur = models.CharField(max_length=255)
    donnee_enregistree = models.FloatField()
    timestamp_temperature = models.DateTimeField(auto_now_add=True)

class Pression(Mesure):
    nom_capteur = models.CharField(max_length=255)
    donnee_enregistree = models.FloatField()
    timestamp_pression = models.DateTimeField(auto_now_add=True)
