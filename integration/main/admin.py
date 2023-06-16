from django.contrib import admin
from .models import *

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('prenom','nom','age','email','adresse','date')

admin.site.register(Patient, PatientAdmin)



class MedecinAdmin(admin.ModelAdmin):
    list_display = ('prenom','nom','age','email','adresse','genre','specialite','departement','service')

admin.site.register(Medecin, MedecinAdmin)



class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom','departement')

admin.site.register(Service, ServiceAdmin)


class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom',)

admin.site.register(Departement, DepartementAdmin)


class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('nom',)

admin.site.register(Medicament, MedicamentAdmin)


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('date','intitule','medecin','patient','diagnostic','medicament','dosage')

admin.site.register(Consultation, ConsultationAdmin)


class FacturationAdmin(admin.ModelAdmin):
    list_display = ('date','departement','patient','service','prix_consultation')

admin.site.register(Facturation, FacturationAdmin)