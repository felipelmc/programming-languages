from django.urls import path
from . import views

urlpatterns = [
    path('', views.felipe, name='index-preco-quadras'),   
]