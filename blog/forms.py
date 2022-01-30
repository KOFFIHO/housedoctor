from django.contrib.admin.options import TabularInline
from django.forms import ModelForm, TextInput,Textarea,DateField
from django.forms import ModelForm
from django.forms.fields import DateTimeField
from django.forms.widgets import DateInput
#from django.forms.widgets import DateTInput
#from .models import Specialiste
from .models import Consultation
from .models import* 
from django.forms import forms 


class ConsultationForm(ModelForm):

    class Meta:
        model = Consultation
        fields = ['name','date','numero','heure','age', 'sexe','communequartier','complement','mootifAge','specialisation']
        widgets = {
            'age' : TextInput({'placeholder':'AGES', 'class':'form-control'}),
            'name': TextInput(attrs={'placeholder':'Nom et Prénoms','class':'form-control input-md'}),
            'numero': TextInput(attrs={'placeholder':'Numero 225 XX XX XX XX','class':'form-control'}),
            'mootifAge' : TextInput(attrs={'placeholder':'Motif de ma visite','class':'form-control'}),
            'date': TextInput(attrs={'placeholder':'MM/JJ/AA','class':'form-control'}),
            'communequartier': TextInput(attrs={'placeholder':'Commune et Quartier','class':'form-control'}), 
            'complement': TextInput(attrs={'placeholder':"Plus d'information sur votre lieu d'habitation",'class':'form-control'}),
            'heure': TextInput({'placeholder':'Heure XX:XX', 'class':'form-control'}),
        }
 
