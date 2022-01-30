from django.urls import path
from django.conf.urls import url
from .views import index ,rendezvous,pharmatopci,detpharma,medicaments,rechercheform
from house import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',index, name="index" ),
    path('rendezvous',rendezvous, name="rendezvous" ),
    path('pharmatopci',pharmatopci, name="pharmatopci" ),
    path('pharmacies/<slug>/',detpharma, name='detpharma'),
    path('rayons/<slug>/', medicaments, name='medicaments'),
    path('rechercheform',rechercheform, name="rechercheform" ),
    #url(r'^medicaments/(?P<medicaments_id>[0-9]+)$', medicaments, name='medicaments'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)