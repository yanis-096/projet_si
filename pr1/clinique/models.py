# clinique/models.py

from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True, default='2024-08-21')
    adresse = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, default='example@example.com') 
    password = models.CharField(max_length=128,null=True, blank=True) 
    tele = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        app_label = 'clinique'
        

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True, default='2020-01-01')
    specialite = models.CharField(max_length=100)
    date_embauche = models.DateField(null=True, blank=True, default='2020-01-01')
    adresse_cabinet = models.CharField(max_length=200, null=True, blank=True, default='Valeur par défaut')
    email = models.EmailField(null=True, blank=True, default='example@example.com')
    password = models.CharField(max_length=128,null=True, blank=True)

    class Meta:
        app_label = 'clinique'
    

class RendezVous(models.Model):
    date_rdv = models.DateField(default='2020-01-01')
    heure_rdv = models.TimeField(default='08:00')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=1)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE,default=1)
    
    class Meta:
        app_label = 'clinique'

class DossierMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    informations_medicales = models.TextField()
    class Meta:
        app_label = 'clinique'

class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    equipement_cardiologie = models.TextField()
    procedures_cardiologie = models.TextField()
    class Meta:
        app_label = 'clinique'
