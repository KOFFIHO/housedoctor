from django.db import models
from datetime import datetime, date

from django.forms.fields import CharField, DateField, TimeField

# Create your models here.
class Consultation(models.Model):
    name = models.CharField(max_length=100)
    
    date = models.DateField(auto_now=False, auto_now_add=False)
    date_ajout=models.DateField(auto_now_add=True)
    heure = models.TimeField()
    numero = models.IntegerField()
    communequartier = models.CharField(max_length=100)
    age = models.IntegerField()
    mootifAge = models.TextField()
    choix_sexe = [
        ('MASCULIN','MASCULIN'),
        ('FEMININ','FEMININ')
    ]
    sexe = models.CharField(max_length=100, choices=choix_sexe)
    choix_specialist = [
        ('GENERALISTE', 'GENERALISTE'),
        ('PEDIATRE','PEDIATRE')
    ]     
    specialisation= models.CharField(max_length=100, choices=choix_specialist)
    
    complement = models.TextField()

    def __str__(self):
            return self.name

    def register(self):
            self.save()

class Medicament(models.Model):
    titre = models.CharField(max_length=200)
    photomedicament = models.ImageField(upload_to='photomedicaments')
    Prix =  models.IntegerField()
    Description = models.TextField()
    slug=models.CharField(max_length=50)

    def __str__(self):
        return self.titre

class Rayon(models.Model):
    nomrayon = models.CharField(max_length=200)
    medicament = models.ManyToManyField(Medicament, related_name='medicaments')
    slug=models.CharField(max_length=50)

    def __str__(self):
        return self.nomrayon

    def get_absolute_url(self):
        return reverse('rayon',slug=[str(self.slug)])



class Pharmacie(models.Model):
    nompharma = models.CharField(max_length=200)
    imagephrama = models.ImageField(upload_to='logopharma')
    imageproprietaire = models.ImageField(upload_to ='PROPRIETAIRE')
    commune = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    contact = models.CharField(max_length=14)
    rayon = models.ManyToManyField(Rayon, related_name='rayons')
    slug=models.CharField(max_length=50)
    degarde = models.BooleanField(default=True)

    @staticmethod
    def get_all_pharmacies():
        return Pharmacie.objects.all()

    def __str__(self):
        return self.nompharma

    def get_absolute_url(self):
        return reverse('detpharma',slug=[str(self.slug)])

class Publicite(models.Model):
    imagepub = models.ImageField(upload_to='logopub')
    nompub = models.CharField(max_length=200)
    description = models.TextField()

    @staticmethod
    def get_all_publicites():
        return Publicite.objects.all()

    def __str__(self):
        return self.nompub