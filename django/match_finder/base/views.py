from django.shortcuts import render

def ranking(request):
    return render(request, 'base/ranking.html')

def index(request):
    return render(request, 'base/index.html')

def perfis(request):
    return render(request, 'base/perfis.html')
    
def perfil_usuario(request):
    return render(request, 'base/perfil_usuario.html')

def projeto(request):
    return render(request, 'base/projeto.html')

def registro(request):
    return render(request, 'base/registro.html')

def mapa(request):
    return render(request, 'base/mapa.html')

def chat(request):
    return render(request, 'base/chat.html')

def login(request):
    return render(request, 'base/login.html')
