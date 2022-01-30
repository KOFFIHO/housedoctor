from django.shortcuts import render,redirect
from .forms import *
from .models import *
#from django.contrib import messages #
#from django import forms
from .forms import ConsultationForm

#from blog import forms

# Create your views here.
def index(request):
     return render(request, 'index.html')


def rendezvous(request):
     form = ConsultationForm()
     message= ""
     error=""
     if request.method == "POST":
          form = ConsultationForm(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               messages='Vous avez valider ma visite.'
               return redirect('index')
          else:
               print(form.errors) 
               error="ok"
             #form = ConsultationForm()
     context={
          'form':form,
          'message':message,
          'error':error
          }
     form = ConsultationForm()
     return render(request, 'rendezvous.html',context)


def pharmatopci(request):
     pharmacies = Pharmacie.objects.all()
     publicites = Publicite.objects.all()
     context={
          'publicites':publicites,
          'pharmacies':pharmacies
     }
     return render(request, 'pharmatopci.html',context)

def rechercheform(request):
    #nombre=0
    message = ""
    query = request.GET.get('query')
    if not query:
        pharmacies = Pharmacie.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        pharmacies = Pharmacie.objects.filter(nompharma__icontains=query)
        if not pharmacies.exists():
            pharmacies = Pharmacie.objects.filter(degarde__icontains=query)
        if not pharmacies.exists():
            pharmacies = Pharmacie.objects.filter(commune__icontains=query)
        if not pharmacies.exists():
            pharmacies = Pharmacie.objects.filter(quartier__icontains=query)
        if not pharmacies.exists():
            message ="Aucun resulat trouvé pour %s"%query
            context = {
                'message':message,
                }

    context = {
        'pharmacies':pharmacies,
        #'repetiteurs':repetiteurs,
        'message':message,
    }
    return render(request, 'pharmatopci.html', context)


def detpharma(request ,slug):
     pharmacies = Pharmacie.objects.get(slug=slug)
     rayons = Rayon.objects.all()
     context={
          'pharmacie':pharmacies,
          'rayons':rayons ,
     }
     return render(request, 'detpharma.html',context)

def medicaments(request, slug):
     #id = int(medicaments_id)
     medicaments = Medicament.objects.all()
     rayon = Rayon.objects.get(slug=slug)
     pharmacies = Pharmacie.objects.all()
     
     context={
          'pharmacie':pharmacies,
          'rayon':rayon ,
          'medicament':medicament
     }
     return render(request, 'rayons.html',context)
