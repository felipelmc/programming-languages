from django.shortcuts import render

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


def ranking(request):
    content['name'] = 'Ranking'
    return render(request, 'base/ranking.html', content)

def index(request):
    content['name'] = 'Início'
    return render(request, 'base/index.html', content)

def perfis(request):
    content['name'] = 'Desenvolvedores'
    return render(request, 'base/perfis.html', content)
    
def perfil_usuario(request):
    content['name'] = 'Perfil'
    return render(request, 'base/perfil_usuario.html', content)

def projeto(request):
    content['name'] = 'O projeto'
    return render(request, 'base/projeto.html', content)

def registro(request):
    content['name'] = ''
    return render(request, 'base/registro.html', content)

def mapa(request):
    content['name'] = 'Mapa'
    return render(request, 'base/mapa.html', content)

def chat(request):
    content['name'] = 'Chat'
    return render(request, 'base/chat.html', content)

def login(request):
    content['name'] = ''
    return render(request, 'base/login.html', content)

def analises(request):
    content['name'] = 'Análises'
    return render(request, 'base/analises.html', content)
