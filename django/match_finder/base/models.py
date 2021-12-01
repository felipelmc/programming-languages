from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    ip_usuario = models.GenericIPAddressField()
    primeiro_nome = models.CharField(max_length=80)
    sobrenome = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    username = models.CharField(max_length=15)
    #hash_senha = make_password()
    CEP = models.IntegerField()
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    status = models.CharField(max_length=150)
    fav_esport = models.CharField(max_length=80)
    altura = models.FloatField()
    idade = models.IntegerField()
    peso = models.FloatField()
    genero = models.SmallIntegerField()
    
    
class Quadra(models.Model):
    tipo = models.CharField(max_length=80)
    rua = models.CharField(max_length=80)
    CEP = models.IntegerField()
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    alugada = models.BooleanField(max_length=3)
    estrelas = models.IntegerField() # 1 - 5
    valor_hora = models.IntegerField()
    horario_funcionamento = models.IntegerField()
    descricao = models.TextField() 