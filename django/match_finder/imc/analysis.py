import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cur = conn.cursor()

query = '''
SELECT *
FROM base_usuario
'''

df = pd.read_sql(query, con = conn)

cur.close()
conn.close()


df = df[["fav_esport", "altura","peso", "genero"]]
df = df[df["altura"]!=0].reset_index()
df = df.drop(columns=["index"])

imc = []

for i in df.index:
    a = (df.loc[i]["altura"])/100
    imc_i = df.loc[i]["peso"]/(a**2)
  
    imc.append(imc_i)
    
df["imc"]=imc


men = df[df["genero"]=="Masculino"]
women = df[df["genero"]=="Feminino"]

men = men.groupby(["fav_esport"]).mean()
women = women.groupby(["fav_esport"]).mean()

e = ["Basquete", "Futebol", "Futsal", "Handebol", "Outros", "Vôlei"]


x = np.arange(6)
width = 0.3  

  
plt.bar(x-0.2, men["imc"], width, color='blue')
plt.bar(x+0.2, women["imc"], width, color='pink')
plt.xticks(x, e)
plt.xlabel("Esporte favorito")
plt.ylabel("IMC")
plt.legend(["M", "F"])
plt.show()


plt.bar(x-0.2, men["altura"], width, color='blue')
plt.bar(x+0.2, women["altura"], width, color='pink')
plt.xticks(x, e)
plt.xlabel("Esporte favorito")
plt.ylabel("Altura")
plt.legend(["M", "F"])
plt.show()



plt.bar(x-0.2, men["peso"], width, color='blue')
plt.bar(x+0.2, women["peso"], width, color='pink')
plt.xticks(x, e)
plt.xlabel("Esporte favorito")
plt.ylabel("Peso")
plt.legend(["M", "F"])
plt.show()














