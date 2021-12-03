import random
import sqlite3 
import pandas as pd
from faker import Faker

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

fake = Faker('pt_BR')

Quadra = {
    'id_quadra': [],
    'tipo': [],
    'rua': [],
    'CEP': [],
    'cidade': [],
    'estado': [],
    'alugada': [],
    'telefone': [],
    'estrelas': [],
    'valor_hora': [],
    'horario_abertura': [],
    'horario_fechamento': [],
    'descricao': []
}

for idquadra in range(1, 201):
    Quadra['id_quadra'].append(idquadra)
    Quadra['tipo'].append(random.choice(['Basquete', 'Vôlei', 'Futebol', 'Futsal', 'Handebol']))
    Quadra['rua'].append(fake.street_name())
    Quadra['CEP'].append(fake.postcode())
    Quadra['cidade'].append(fake.city())
    Quadra['estado'].append(fake.estado_sigla())
    Quadra['alugada'].append(random.choice([True, False]))
    Quadra['telefone'].append(fake.phone_number())
    Quadra['estrelas'].append(random.randint(0,5))
    Quadra['valor_hora'].append(random.randint(5,50))
    Quadra['horario_abertura'].append(random.randint(7, 11))
    Quadra['horario_fechamento'].append(random.randint(16, 20))
    Quadra['descricao'].append(random.choice(['Espaço fechado', 'Com churrasqueira', 'Cerveja gelada', 'Localização ótima', 'Bom custo-benefício']))

quadras = pd.DataFrame(Quadra)
quadras = quadras.drop(['id_quadra'], axis=1)


quadras.to_sql('base_quadra', conn, if_exists = 'replace', index = False)

cur.close()
conn.close()