from django.urls import path
from . import views

urlpatterns = [
    path('', views.guilherme, name='index-esporte-pref'),   
]