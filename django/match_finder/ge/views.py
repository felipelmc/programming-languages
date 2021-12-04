from django.shortcuts import render

# Create your views here.

pages = [
    { 'url': 'index', 'name': "INÍCIO"},
    { 'url': 'projeto', 'name': "O PROJETO"},
    { 'url': 'mapa', 'name': "MAPA"},
    { 'url': 'ranking', 'name': "RANKING"},
    { 'url': 'perfis', 'name': "DESENVOLVEDORES"},
    { 'url': 'chat', 'name': "CHAT"},
    { 'url': 'analises', 'name': "ANÁLISES"},
]

content = {'pages': pages}

def index(request):
    content['name'] = 'Esportes Favoritos por Gênero' 
    return render(request, 'ge/index.html', content)