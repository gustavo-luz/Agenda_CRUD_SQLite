
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


#update TODO update based on dif where's (email, twitter, insta, deixar o usuario escolher)
@commit_close
def db_update(name,email):
    return"""
    UPDATE users SET email='{}' WHERE name='{}'
    """.format(email,name)

#delete
@commit_close
def db_delete(name):
    return"""
    DELETE from users WHERE name='{}'
    """.format(name)


#read
#read consulta individual
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

#read consulta total
def db_select_all():
    con=sqlite3.connect('agenda.db')
    cur=con.cursor()
    sql= """SELECT *
    FROM users
    """

    cur.execute(sql)
    data=cur.fetchall()
    con.close()
    return data


if __name__ == '__main__':
    option=True

while option:
    

    print ("""
    Menu:\n
    1. Inserir Contato
    2. Consultar Contato
    3. Remover Contato
    4. Alterar Contato
    5. Gerar Relatório
    6. Sair
    """)
    option=input("Escolha uma opção do Menu: ")

#TODO criar opção de cadastrar mais de um contato, pedir o input do numero e repertir os pedidos de input quantas vezes precisar
    if option=="1":
        nome=input("Informe o nome: ")
        telefone=input("Informe o telefone: ")
        email=input("Informe o e-mail: ")
        twitter=input("Informe a conta do twitter: ")
        instagram=input("Informe a conta do instagram: ")
        db_insert(nome,telefone,email,twitter,instagram)
        #TODO COLOCAR TABULAÇÃO DESTACANDO O PRINT: https://www.educba.com/python-print-table/
        print("\n Contato inserido:","nome:",nome,'\t',"telefone:",telefone,'\t',"email:",email,'\t',"twitter:",twitter,'\t',"instagram:",instagram) 


    elif option=="2":
        nome=input("Qual nome deseja encontrar? ")
        #TODO arrumar a consulta pra não ter que ser o id
        consulta=(db_select('id',nome))
        #TODO COLOCAR TABULAÇÃO DESTACANDO O PRINT E COM OS HEADERS
        print("\n Contato encontrado",consulta) 

    elif option=="3":
        nome=input("Qual nome deseja remover? ")
        db_delete(nome)
        #TODO COLOCAR TABULAÇÃO DESTACANDO O PRINT E COM OS HEADERS
        print(nome,"removido(a) da agenda com sucesso") 

    elif option=="4":
        nome= input("Qual usuário deseja alterar? ")
        mail=input("Qual o novo email? ")
        db_update(nome,mail)
        print("\n Contato Alterado") 

    elif option=="5":
        report=db_select_all()
        print("\n Relatório Gerado:")
        #TODO COLOCAR TABULAÇÃO DESTACANDO O PRINT E COM OS HEADERS
        pprint(report)
        

    elif option=="6":
        
        pprint("\n Até Logo")
        break 

    elif option !="":
        print("\n Opção inválida, escolha outra opção") 