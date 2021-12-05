from re import A
from django.shortcuts import render
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import sqlite3
import seaborn as sns
from sklearn.preprocessing import MultiLabelBinarizer

pages = [
    { 'url': 'index', 'name': "Início"},
    { 'url': 'projeto', 'name': "O projeto"},
    { 'url': 'mapa', 'name': "Mapa"},
    { 'url': 'ranking', 'name': "Ranking"},
    { 'url': 'perfis', 'name': "Desenvolvedores"},
    { 'url': 'chat', 'name': "Chat"},
    { 'url': 'analises', 'name': "Análises"},
]


def guilherme(request):
    
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    query = '''
    SELECT * 
    FROM base_usuario
    '''

    df = pd.read_sql(query, con = conn)

    cur.close()
    conn.close()

    df = df[['esportes_praticados','fav_esport']]
    df['esportes_praticados'] = df['esportes_praticados'].str.replace(' ','').str.split(',')

    mlb = MultiLabelBinarizer(sparse_output=True)

    df= df.join(
                pd.DataFrame.sparse.from_spmatrix(
                    mlb.fit_transform(df.pop('esportes_praticados')),
                    index=df.index,
                    columns=mlb.classes_))

    tupla = ('Basquete','Futebol','Futsal','Handebol','Outros','Vôlei')

    fig, ax = plt.subplots(figsize = (8, 6))
    df.loc[df['fav_esport'] == 'Basquete'].sum().drop('fav_esport').plot(kind='bar')
    
    ax.set(title = "Esporte favorito: Basquete",
            xlabel = "Outros esportes praticados",
            ylabel = "Praticantes")
    ax.set_xticklabels(tupla)
    ax.set_xticks(range(0,len(tupla)))
    basq = mpld3.fig_to_html(fig)

    fig, ax = plt.subplots(figsize = (8, 6))
    df.loc[df['fav_esport'] == 'Futebol'].sum().drop('fav_esport').plot(kind='bar')
    ax.set_xticklabels(tupla)
    ax.set_xticks(range(0,len(tupla)))
        
    ax.set(title = "Esporte favorito: Futebol",
            xlabel = "Outros esportes praticados",
            ylabel = "Praticantes")
    fut = mpld3.fig_to_html(fig)

    fig, ax = plt.subplots(figsize = (8, 6))
    df.loc[df['fav_esport'] == 'Futsal'].sum().drop('fav_esport').plot(kind='bar')        
    ax.set(title = "Esporte favorito: Futsal",
            xlabel = "Outros esportes praticados",
            ylabel = "Praticantes")
    ax.set_xticklabels(tupla)
    ax.set_xticks(range(0,len(tupla)))
    futsal = mpld3.fig_to_html(fig)

    fig, ax = plt.subplots(figsize = (8, 6))
    df.loc[df['fav_esport'] == 'Handebol'].sum().drop('fav_esport').plot(kind='bar')        
    ax.set(title = "Esporte favorito: Handebol",
            xlabel = "Outros esportes praticados",
            ylabel = "Praticantes")
    ax.set_xticklabels(tupla)
    ax.set_xticks(range(0,len(tupla)))
    hand = mpld3.fig_to_html(fig)

    fig, ax = plt.subplots(figsize = (8, 6))
    df.loc[df['fav_esport'] == 'Outros'].sum().drop('fav_esport').plot(kind='bar')        
    ax.set(title = "Esporte favorito: Outros",
            xlabel = "Outros esportes praticados",
            ylabel = "Praticantes")
    ax.set_xticklabels(tupla)
    ax.set_xticks(range(0,len(tupla)))
    outros = mpld3.fig_to_html(fig)

    fig, ax = plt.subplots(figsize = (8, 6))
    df.loc[df['fav_esport'] == 'Vôlei'].sum().drop('fav_esport').plot(kind='bar') 
    ax.set_xticklabels(tupla)
    ax.set_xticks(range(0,len(tupla)))
    ax.set(title = "Esporte favorito: Volêi",
            xlabel = "Outros esportes praticados",
            ylabel = "Praticantes")


    volei = mpld3.fig_to_html(fig)


    content = {
    "fut": fut,
    "futsal" : futsal,
    "hand" : hand,
    "outros": outros,
    "volei": volei
    }
    
    content['name'] = 'Preferencias'
    return render(request, 'esporte_pref/esporte-pref.html', content)