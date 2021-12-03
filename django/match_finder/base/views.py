from django.shortcuts import render

pages = [
    { 'url': 'index', 'name': "INÍCIO"},
    { 'url': 'projeto', 'name': "O PROJETO"},
    { 'url': 'mapa', 'name': "MAPA"},
    { 'url': 'ranking', 'name': "RANKING"},
    { 'url': 'perfis', 'name': "DESENVOLVEDORES"},
    { 'url': 'chat', 'name': "CHAT"},
]

content = {'pages': pages}


def ranking(request):
    content['name'] = 'RANKING'
    return render(request, 'base/ranking.html', content)

def index(request):
    content['name'] = 'INÍCIO'
    return render(request, 'base/index.html', content)

def perfis(request):
    content['name'] = 'DESENVOLVEDORES'
    return render(request, 'base/perfis.html', content)
    
def perfil_usuario(request):
    content['name'] = 'PERFIL'
    return render(request, 'base/perfil_usuario.html', content)

def projeto(request):
    content['name'] = 'O PROJETO'
    return render(request, 'base/projeto.html', content)

def registro(request):
    content['name'] = ''
    return render(request, 'base/registro.html', content)

def mapa(request):
    content['name'] = 'MAPA'
    return render(request, 'base/mapa.html', content)

def chat(request):
    content['name'] = 'CHAT'
    return render(request, 'base/chat.html', content)

def login(request):
    content['name'] = ''
    return render(request, 'base/login.html', content)
