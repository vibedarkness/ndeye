from django.db import models
class TABLEDEPARTEMENT(models.Model):
    Id_departement =models.CharField(max_length=10)
    Nom=models.CharField(max_length=10)
# Create your models here.
    def __str__(self):
        return self.Nom
class TABLESERVICE(models.Model):
    Id_service=models.CharField(max_length=10)
    Id_derpartement=models.CharField(max_length=10)
    Nom=models.CharField(max_length=10)
    def __str__(self):
       return self.Id_service
class TABLEPATIENT(models.Model):
    Id_patient=models.CharField(max_length=10)
    Date=models.CharField(max_length=10)
    Photo=models.CharField(max_length=10)
    Nom=models.CharField(max_length=10)
    Prenom=models.CharField(max_length=10)
    Age=models.CharField(max_length=10)
    Email=models.CharField(max_length=10)
    Adresse=models.CharField(max_length=10)
    def __str__(self):
       return self.Nom
class TABLEFACTURATION(models.Model):
    Id_facturation=models.CharField(max_length=10)
    Date=models.CharField(max_length=10)
    Id_patient=models.CharField(max_length=10)
    Id_derpartement=models.CharField(max_length=10)
    Id_service=models.CharField(max_length=10)
    Prix_consultation=models.CharField(max_length=10)
    def __str__(self):
       return self.Date
class TABLECONSULTATION(models.Model):
    Id_consultation=models.CharField(max_length=10)
    Date=models.CharField(max_length=10)
    Intitule=models.CharField(max_length=10)
    Id_medecin=models.CharField(max_length=10)
    Id_patient=models.CharField(max_length=10)
    Diagnostic=models.CharField(max_length=10)
    Id_medicament=models.CharField(max_length=10)
    Dosage=models.CharField(max_length=10)
    def __str__(self):
       return self.Date
class TABLEMEDECIN(models.Model):
    Id_medecin=models.CharField(max_length=10)
    Nom=models.CharField(max_length=10)
    photo=models.CharField(max_length=10)
    Prenom=models.CharField(max_length=10)
    Age=models.CharField(max_length=10)
    Genre=models.CharField(max_length=10)
    Email=models.CharField(max_length=10)
    Adresse=models.CharField(max_length=10)
    Specialite=models.CharField(max_length=10)
    Id_departement=models.CharField(max_length=10)
    Id_service=models.CharField(max_length=10)
    def __str__(self):
       return self.Nom
class TABLEMEDICAMENT(models.Model):
    Id_medicament=models.CharField(max_length=10)
    photo=models.CharField(max_length=10)
    Nom=models.CharField(max_length=10)
    def __str__(self):
       return self.Nom