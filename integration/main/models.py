from django.db import models

# Create your models here.



class Departement(models.Model):

    nom=models.CharField(max_length=100)
# Create your models here.
    def __str__(self):
        return self.nom
    


class Service(models.Model):

    departement=models.ForeignKey(Departement, on_delete=models.CASCADE)
    nom=models.CharField(max_length=100)
    def __str__(self):
       return self.nom
    

class Patient(models.Model):
    date=models.DateField(auto_now_add=True)
    photo= models.ImageField(max_length=200)
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField( max_length=254)
    adresse=models.TextField()
    def __str__(self):
       return self.nom
    



class Facturation(models.Model):

    date=models.DateField(auto_now_add=True)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    departement=models.ForeignKey(Departement, on_delete=models.CASCADE)
    service=models.ForeignKey(Service, on_delete=models.CASCADE)
    prix_consultation=models.IntegerField()
    def __str__(self):
       return self.patient.nom


class Medecin(models.Model):
    genrechoice=(
        ("M","MASCULIN"),
        ("F","FEMININ")

    )

    nom=models.CharField(max_length=100)
    photo=models.ImageField(max_length=100)
    prenom=models.CharField(max_length=100)
    age=models.IntegerField()
    genre=models.CharField(max_length=10,choices=genrechoice)
    email=models.EmailField( max_length=254)
    adresse=models.TextField()
    specialite=models.CharField(max_length=100)
    departement=models.ForeignKey(Departement, on_delete=models.CASCADE)
    service=models.ForeignKey(Service, on_delete=models.CASCADE)
    def __str__(self):
       return self.nom
    

class Medicament(models.Model):
    photo=models.ImageField(max_length=100)
    nom=models.CharField(max_length=100)
    def __str__(self):
       return self.nom    



class Consultation(models.Model):
    date=models.DateField(auto_now_add=True)
    intitule=models.CharField(max_length=100)
    medecin=models.ForeignKey(Medecin, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnostic=models.CharField(max_length=100)
    medicament=models.ForeignKey(Medicament, on_delete=models.CASCADE)
    dosage=models.CharField(max_length=100)
    def __str__(self):
       return self.patient.nom
