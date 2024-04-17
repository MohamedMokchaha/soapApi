# Dans urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('envoyer-xml/', views.envoyer_xml, name='envoyer_xml'),
]
