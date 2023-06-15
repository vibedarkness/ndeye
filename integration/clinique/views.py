from django.shortcuts import render,redirect
import datetime
from django.http import HttpResponse

# from django.core.mail import send_mail
# from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'base.html')

# def departement(request):
#     return render(request, 'services.html')

# def departement(request):
#     return render(request, 'patient.html')

# def departement(request):
#     return render(request, 'facturation.html')

# def departement(request):
#     return render(request, 'medecin.html')

# def departement(request):
#     return render(request, 'consultation.html')

# def departement(request):
#     return render(request, 'medicament.html')


