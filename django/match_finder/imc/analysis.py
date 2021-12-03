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
df

cur.close()
conn.close()