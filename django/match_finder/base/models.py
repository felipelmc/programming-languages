from typing_extensions import Required
from django.db import models
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(self,username,email,telefone,primeiro_nome,sobrenome,password=None):
        if not email:
            raise ValueError('O email é obrigatório')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            telefone=telefone,
            primeiro_nome=primeiro_nome,
            sobrenome=sobrenome
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,telefone,primeiro_nome,sobrenome,password=None):
        user = self.create_user(
            username=username,
            email=email,
            telefone=telefone,
            primeiro_nome=  primeiro_nome,
            sobrenome=sobrenome,
            password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Usuario(AbstractBaseUser):
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
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['primeiro_nome', 'sobrenome', 'email', 'telefone']
    objects = UsuarioManager()

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