from django.db import models

class Concessionnaire(models.Model):
    nom = models.CharField(max_length=128)
    numero_siret = models.IntegerField()
    code_postal = models.CharField(max_length=5)
    
class Voiture(models.Model):
    marque = models.CharField(max_length=128)
    modele = models.CharField(max_length=128)
    chevaux = models.IntegerField()
    concessionnaire = models.ForeignKey(Concessionnaire, on_delete=models.CASCADE)

