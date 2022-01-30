from django.contrib import admin
from .models import Consultation
from .models import Medicament
from .models import Rayon
from .models import Pharmacie 
from .models import Publicite

class AdminConsultation(admin.ModelAdmin):
       list_display = ['name','date','heure','numero','communequartier','mootifAge','complement','specialisation']

class AdminPharmacie(admin.ModelAdmin):
       list_display = ['nompharma','commune','quartier','contact','imagephrama']

class AdminMedicament(admin.ModelAdmin):
       list_display = ['titre','photomedicament','Prix','Description']

admin.site.register(Consultation, AdminConsultation)
admin.site.register(Pharmacie, AdminPharmacie) 
admin.site.register(Rayon)
admin.site.register(Publicite)
admin.site.register(Medicament, AdminMedicament)