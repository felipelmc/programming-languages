from django.shortcuts import render

# Create your views here.

pages = [
    { 'url': 'index', 'name': "Início"},
    { 'url': 'projeto', 'name': "O projeto"},
    { 'url': 'mapa', 'name': "Mapa"},
    { 'url': 'ranking', 'name': "Ranking"},
    { 'url': 'perfis', 'name': "Desenvolvedores"},
    { 'url': 'chat', 'name': "Chat"},
    { 'url': 'analises', 'name': "Análises"},
]

content = {'pages': pages}

def index(request):
    content['name'] = 'Esportes Favoritos por Gênero' 
    return render(request, 'ge/index.html', content)