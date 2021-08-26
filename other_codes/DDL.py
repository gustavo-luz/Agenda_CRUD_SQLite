
#ddl - manipulando a tabela
import sqlite3

#conectar no banco
con = sqlite3.connect('agenda.db')

#cursor
cur = con.cursor()

#criar tabela


#sql= """CREATE TABLE users (
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#    name text not null,
#    phone text not null,
#    email text not null,
#    twitter text not null,
#    instagram text not null);
#"""

sql= """DROP TABLE users;"""

cur.execute(sql)
#commita
con.commit()
#fecha
con.close()