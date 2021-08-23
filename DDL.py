
#ddl - manipulando a tabela
import sqlite3

#conectar no banco
con = sqlite3.connect('agenda.db')

#cursor
cur = con.cursor()

#criar tabela
sql= """CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name varchar(100) not null,
    email varchar(100) not null,
    twitter varchar(100) not null,
    facebook varchar(100) not null);
"""

cur.execute(sql)
#commita
con.commit()
#fecha
con.close()