import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

for row in cur.execute('PRAGMA table_info(base_usuario)'):
    print(row)
    
for row in cur.execute('PRAGMA table_info(base_quadra)'):
    print(row)
    
cur.close()
con.close()
