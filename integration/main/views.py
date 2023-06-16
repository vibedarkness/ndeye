from django.shortcuts import render

from .models import *

# Create your views here.





def index(request):
    patient=Patient.objects.all().count
    facture=Facturation.objects.all().count
    medecin=Medecin.objects.all().count
    medicament=Medicament.objects.all().count
    consult=Consultation.objects.all().count
    depart=Departement.objects.all().count
    service=Service.objects.all().count

    context={
        'total_patient':patient,
        'total_facture':facture,
        'total_medecin':medecin,
        'total_medicament':medicament,
        'total_consult':consult,
        'total_depart':depart,
        'total_service':service,
    }
    return render(request,"index.html",context)



def patient(request):
    patient=Patient.objects.all()

    context={
        'patient':patient,
    }
    return render(request,"patient.html",context)


def medecin(request):
    medecin=Medecin.objects.all()

    context={
        'medecin':medecin,
    }
    return render(request,"medecin.html",context)



def departement(request):
    departement=Departement.objects.all()

    context={
        'departement':departement,
    }
    return render(request,"departement.html",context)



def service(request):
    service=Service.objects.all()

    context={
        'service':service,
    }
    return render(request,"service.html",context)


def medicament(request):
    medic=Medicament.objects.all()

    context={
        'medic':medic,
    }
    return render(request,"medicament.html",context)



def consultation(request):
    consult=Consultation.objects.all()

    context={
        'consult':consult,
    }
    return render(request,"consultation.html",context)



def facture(request):
    facture=Facturation.objects.all()

    context={
        'facture':facture,
    }
    return render(request,"facturation.html",context)