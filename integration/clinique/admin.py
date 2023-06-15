from django.contrib import admin


from django.contrib import admin
from .models import TABLEDEPARTEMENT, TABLESERVICE, TABLEPATIENT,TABLEFACTURATION,TABLECONSULTATION,TABLEMEDECIN, TABLEMEDICAMENT

admin.site.register(TABLEDEPARTEMENT)
admin.site.register(TABLESERVICE)
admin.site.register(TABLEPATIENT)
admin.site.register(TABLEFACTURATION)
admin.site.register(TABLECONSULTATION)
admin.site.register( TABLEMEDECIN)
admin.site.register( TABLEMEDICAMENT)
# Register your models here.
