
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking/', views.ranking, name='ranking'),
    path('perfis/', views.perfis, name='perfis'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('projeto/', views.projeto, name='projeto'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('mapa/', views.mapa, name='mapa'), 
    path('chat/', views.chat, name='chat'),   
]