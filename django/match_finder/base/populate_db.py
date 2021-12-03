from django.contrib.auth import get_user_model
import numpy as np
import pandas as pd
from faker import Faker
import random
import os

fake = Faker('pt_BR')
Usuario = {
    'id_usuario': [],
    'ip_usuario': [],
    'primeiro_nome': [],
    'sobrenome': [],
    'email': [],
    'username': [],
    'telefone': [],
    'CEP': [],
    'cidade': [],
    'estado': [],
    'status': [],
    'imagem': []
}

for idusuario in range(1, 210):
    Usuario['id_usuario'].append(idusuario)
    Usuario['ip_usuario'].append(fake.ipv4())
    Usuario['primeiro_nome'].append(fake.first_name())
    Usuario['sobrenome'].append(fake.last_name())
    Usuario['email'].append(fake.ascii_email())
    Usuario['username'].append(fake.user_name())
    Usuario['telefone'].append(fake.phone_number())
    Usuario['CEP'].append(fake.postcode())
    Usuario['cidade'].append(fake.city())
    Usuario['estado'].append(fake.estado_sigla())
    Usuario['status'].append(random.choice(['Gente boa', 'Buscando partidas', 'Buscando novas amizades', 'Offline', 'Online']))
    Usuario['imagem'].append(fake.image_url())

usuarios = pd.DataFrame(Usuario)
usuarios = usuarios.drop(['id_usuario'], axis=1)

cwd = os.getcwd()
usuario_form = pd.read_csv(os.path.join('user_form.csv'))
usuario_form = usuario_form.transpose().iloc[1:7]
usuario_form = usuario_form.transpose()
super_sample = usuario_form.sample(n=150,replace=True)


noise_w = np.random.randint(-3, 4, size=super_sample.shape[0])
noise_h = np.random.randint(-2, 3, size=super_sample.shape[0])
super_sample['peso'] = super_sample['peso'] + noise_w
super_sample['altura'] = super_sample['altura'] + noise_h
forms_final = pd.concat([usuario_form, super_sample]).reset_index(drop=True)
usuario_form
super_sample
forms_final
dados = pd.concat([usuarios, forms_final], axis=1)
dados.iloc[0]
# Create your tests here.
user = get_user_model()
for i in range(0, dados.shape[0]):
    input = user.objects.create_user(ip_usuario=dados.iloc[i][0],
        primeiro_nome=dados.iloc[i][1],
        sobrenome=dados.iloc[i][2],
        email=dados.iloc[i][3],
        username=dados.iloc[i][4],
        telefone=dados.iloc[i][5],
        CEP=dados.iloc[i][6],
        cidade=dados.iloc[i][7],
        estado=dados.iloc[i][8],
        status=dados.iloc[i][9],
        imagem=dados.iloc[i][10],
        esportes_praticados=dados.iloc[i][11],
        fav_esport=dados.iloc[i][12],
        idade=dados.iloc[i][13],
        peso=dados.iloc[i][14],
        altura=dados.iloc[i][15],
        genero=dados.iloc[i][16])
