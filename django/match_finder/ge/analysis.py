import matplotlib.pyplot as plt
from faker import Faker
import pandas as pd
import numpy as np
import sqlite3
import random

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

query = '''
SELECT * 
FROM base_usuario
'''

df = pd.read_sql(query, con = conn)

cur.close()
conn.close()

df.head()