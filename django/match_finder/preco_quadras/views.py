from django.shortcuts import render
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import numpy as np
import sqlite3
import seaborn as sns

pages = [
    { 'url': 'index', 'name': "Início"},
    { 'url': 'projeto', 'name': "O projeto"},
    { 'url': 'mapa', 'name': "Mapa"},
    { 'url': 'ranking', 'name': "Ranking"},
    { 'url': 'perfis', 'name': "Desenvolvedores"},
    { 'url': 'chat', 'name': "Chat"},
    { 'url': 'analises', 'name': "Análises"},
]


def felipe(request):
    
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    query = '''
    SELECT * 
    FROM base_quadra
    '''

    df = pd.read_sql(query, con = conn)

    cur.close()
    conn.close()
    
    flt = df[['estado', 'descricao', 'estrelas', 'valor_hora', 'tipo']]
    agrupado = flt.groupby(['estado']).mean().reset_index()
    
    # plot 1
    fig, ax = plt.subplots(figsize = (7, 5))

    sns.barplot(data = agrupado.sort_values(by = 'valor_hora', ascending = False),
                y = 'estado', x = 'valor_hora',
                color = 'orange',
                ax = ax)

    ax.set(title = "Valor médio da hora do aluguel de quadras por estado",
            xlabel = "Valor médio",
            ylabel = "Estado")

    valor_estado = mpld3.fig_to_html(fig)
    
    # plot 2
    fig, ax = plt.subplots(figsize = (7, 5))

    sns.barplot(data = agrupado.sort_values(by = 'estrelas', ascending = False),
            y = 'estado', x = 'estrelas',
            color = 'blue',
            ax = ax)

    ax.set(title = "Média de estrelas das quadras por estado",
       xlabel = "Média de estrelas",
       ylabel = "Estado")
    
    estrela_estado = mpld3.fig_to_html(fig)
    
    #plot 3
    fig, ax = plt.subplots(figsize = (7, 5))

    sns.histplot(data = flt, 
             x = 'tipo',
             shrink = 0.8,
             ax = ax)

    ax.set(title = "Quantidade de quadras para cada esporte",
            xlabel = "Esporte",
            ylabel = "n")

    n_quadras = mpld3.fig_to_html(fig)
    
    # plot 4
    fig, ax = plt.subplots(figsize = (7,5))

    sns.histplot(ax = ax, data = flt, 
             x = 'tipo', hue = 'descricao',
             shrink = 0.7,
             multiple = 'dodge')

    ax.set(title = "Descrição das quadras para cada esporte",
       xlabel = "Esporte",
       ylabel = "n")    
    
    desc_quadras = mpld3.fig_to_html(fig)
    
    content = {
        "pages": pages,
        "valor_estado" : valor_estado,
        "estrela_estado" : estrela_estado,
        "n_quadras": n_quadras,
        "desc_quadras": desc_quadras
    }
    
    content['name'] = 'Quadras'
    
    return render(request, 'preco-quadras/preco-quadras.html', content)