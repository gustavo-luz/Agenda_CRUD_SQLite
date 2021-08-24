
import sqlite3
from pprint import pprint

# TODO INSERT DB CREATION (DDL)

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

if __name__ == '__main__':
    option=True

while option:
    print ("""
    1.Inserir Contato
    2.Consultar Contato
    3.Remover Contato
    4.Alterar Contato
    5. Gerar Relatório
    6. Sair
    """)
    option=input("Escolha uma opção do Menu ")

#TODO criar opção de cadastrar mais de um contato, pedir o input do numero e repertir os pedidos de input quantas vezes precisar
    if option=="1":
        nome=input("Informe o nome ")
        telefone=input("Informe o telefone ")
        email=input("Informe o e-mail ")
        twitter=input("Informe a conta do twitter ")
        instagram=input("Informe a conta do instagram ")
        db_insert(nome,telefone,email,twitter,instagram)
        print("\n Contato inserido:","nome:",nome,'\t',"telefone:",telefone,'\t',"email:",email,'\t',"twitter:",twitter,'\t',"instagram:",instagram) 


    elif option=="2":
        print("\n Contato encontrado") 
    elif option=="3":
        print("\n Contato Removido") 
    elif option=="4":
        print("\n Contato Alterado") 
    elif option=="5":
        print("\n Relatório Gerado")
        #TODO SELECT * FROM USERS 
    elif option=="6":
        print("\n Até Logo")
        break 
    elif option !="":
        print("\n Escolha outra opção") 