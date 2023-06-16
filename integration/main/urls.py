

from .views import *
from django.urls import path
# from django.contrib.auth.decorators import login_required

from main import views


urlpatterns = [

    path('', views.index, name='index'),

    path('patient', views.patient, name='patient'),
    path('medecin', views.medecin, name='medecin'),
    path('departement', views.departement, name='departement'),
    path('service', views.service, name='service'),
    path('medicament', views.medicament, name='medic'),
    path('consultation', views.consultation, name='consultation'),
    path('facture', views.facture, name='facture'),

    ]