from django.db import models

class Usuario(models.Model):
    id_usuario = models.IntegerField()
    primeiro_nome = models.CharField(max_length=80)
    sobrenome = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    username = models.CharField(max_length=15)
    #senha =
    CEP = models.IntegerField()
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    status = models.CharField(max_length=150)
    fav_esport = models.CharField(max_length=80)
    
    
class Quadra(models.Model):
    id_quadra = models.IntegerField()
    tipo = models.CharField(max_length=80)
    rua = models.CharField(max_length=80)
    CEP = models.IntegerField()
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    alugada = models.BooleanField(max_length=3) #Sim, Não
    estrelas = models.IntegerField() # 1 - 5
    valor_hora = models.IntegerField()
    
    
    
    


    