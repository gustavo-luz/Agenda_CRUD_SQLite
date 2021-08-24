""" DML - Manipulação de Dados
Create Read Update Delete
"""
import sqlite3


#função pra conectar na base, conectar o cursos e executar a função com os argumentos
def commit_close(func):
    def decorator(*args):
        con=sqlite3.connect('agenda.db')
        cur=con.cursor()
        sql=func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator

#create insert
@commit_close
def db_insert(name,phone,email,twitter,instagram):
    return """
    INSERT INTO users (name,phone,email,twitter,instagram)
    VALUES('{}', '{}', '{}', '{}', '{}')
    """.format(name,phone,email,twitter,instagram)


#update TODO update based on dif where's
@commit_close
def db_update(name,email):
    return"""
    UPDATE users SET name='{}' WHERE email='{}'
    """.format(name,email)

#delete
@commit_close
def db_delete(name):
    return"""
    DELETE from users WHERE name='{}'
    """.format(name)

#    VALUES('Gustavo', 'gustavo@iesb.br', 'gustavoluz', 'Gustavo Luz')

#    VALUES('Francisco', 'francisco.filho@iesb.br', 'flcaldas', 'Francisco Lopes')

#cur.execute(db_insert('Gustavo', 'gustavo@iesb.br', 'gustavoluz', 'Gustavo Luz'))
#cur.execute(db_update('Gus', 'gustavo@iesb.br'))
#cur.execute(db_delete('Gus'))
#con.commit()

#read
#read consulta
def db_select(data,field):
    con=sqlite3.connect('agenda.db')
    cur=con.cursor()
    sql= """SELECT id, name, phone, email, twitter, instagram
    FROM users
    WHERE {}={}""".format(field,data)

    cur.execute(sql)
    data=cur.fetchall()
    con.close()
    return data
