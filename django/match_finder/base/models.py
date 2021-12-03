from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, telefone, primeiro_nome, sobrenome, password=None, **other_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            telefone=telefone,
            primeiro_nome=primeiro_nome,
            sobrenome=sobrenome,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def update_user(self, ip_usuario, telefone, CEP, cidade, estado, status, esportes_praticados, fav_esport, idade, peso, genero, imagem):
        user = self.mode(
            ip_usuario = ip_usuario,
            telefone = telefone,
            CEP = CEP,
            cidade = cidade,
            estado = estado,
            status = status,
            esportes_praticados = esportes_praticados,
            fav_esport = fav_esport,
            idade = idade,
            peso = peso,
            genero = genero,
            imagem = imagem
        )
        user.save(using = self._db)
        return user
        
    
    def create_superuser(self,username,email,telefone,primeiro_nome,sobrenome,password=None,**other_fields):
        user = self.create_user(
            username=username,
            email=email,
            telefone=telefone,
            primeiro_nome=  primeiro_nome,
            sobrenome=sobrenome,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser,PermissionsMixin):
    ip_usuario = models.GenericIPAddressField(max_length=45,null=True,blank=True)
    primeiro_nome = models.CharField(max_length=80, verbose_name='primeiro_nome')
    sobrenome = models.CharField(max_length=80,verbose_name='sobrenome')
    email = models.EmailField(max_length=80,verbose_name='email', unique=True)
    username = models.CharField(max_length=15,verbose_name='username', unique=True)
    telefone = models.CharField(max_length=15,verbose_name='telefone', unique=True, default=None)
    CEP = models.CharField(max_length=8,verbose_name='CEP')
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    status = models.CharField(max_length=150)
    esportes_praticados = models.CharField(max_length=150, null=True, blank=True)
    fav_esport = models.CharField(max_length=80)
    altura = models.IntegerField(default=0)
    idade = models.IntegerField(default=0)
    peso = models.FloatField(default=0)
    genero = models.CharField(max_length = 1 ,default=0)
    imagem = models.ImageField(default=None)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['primeiro_nome', 'sobrenome', 'email', 'telefone']
    objects = UsuarioManager()

class Quadra(models.Model):
    tipo = models.CharField(max_length=80)
    rua = models.CharField(max_length=80)
    CEP = models.IntegerField()
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    alugada = models.BooleanField(default=False)
    telefone = models.CharField(max_length=15,verbose_name='telefone', unique=True, default=None)
    estrelas = models.IntegerField(default=0) # 0 - 5
    valor_hora = models.IntegerField(default=0)
    horario_abertura = models.IntegerField(default=0)
    horario_fechamento = models.IntegerField(default=0)
    descricao = models.TextField(max_length=80) 

