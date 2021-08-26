
import sqlite3
from pprint import pprint


#conecta no banco e cria a tabela users
def db_creation():
    #conectar no banco
    con = sqlite3.connect('agenda.db')
    #cursor
    cur = con.cursor()
    #criar tabela
    sql= """CREATE TABLE users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name text not null,
        phone text not null,
        email text not null,
        twitter text not null,
        instagram text not null);
    """
    cur.execute(sql)
    #commita
    con.commit()
    #fecha
    con.close()

#deleta a tabela users do banco 
def db_drop():
    con = sqlite3.connect('agenda.db')
    cur = con.cursor()
    sql= """DROP TABLE users;"""
    cur.execute(sql)
    con.commit()
    con.close()



#função pra conectar na base, conectar o cursor e executar a função com os argumentos
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


#as consultas não utilizaram o commit_close, já que possuem um fetchall
#read consulta individual por nome
def db_select(name):
    con=sqlite3.connect('agenda.db')
    cur=con.cursor()
    sql= """SELECT *
    FROM users
    WHERE name='{}'""".format(name)

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

    #TODO adicionar opção de criar ou dropar o db
    #db_creation()
    #db_drop

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


    if option=="1":
        qtd_contatos=int(input("Quantos contatos deseja inserir?\n "))

        n=0

        while n < qtd_contatos:
            print("Contato ",n+1)
            nome=input("Informe o nome: ")
            telefone=input("Informe o telefone: ")
            email=input("Informe o e-mail: ")
            twitter=input("Informe a conta do twitter: ")
            instagram=input("Informe a conta do instagram: ")
            db_insert(nome,telefone,email,twitter,instagram)
            print("\n Contato inserido:")
            print ("{:<8} {:<10} {:<14} {:<8} {:<8}".format('Nome','Telefone','E-mail','Twitter','Instagram'))
            print ("{:<8} {:<10} {:<14} {:<8} {:<8}".format(nome,telefone,email,twitter,instagram))
            n+=1


    elif option=="2":
        nome=input("Qual nome deseja encontrar? ")
        consulta=(db_select(nome))
        print("\n Retorno da Busca:")
        print ("{:<5} {:<8} {:<10} {:<14} {:<8} {:<8}".format('ID','Nome','Telefone','E-mail','Twitter','Instagram'))
        pprint(consulta) 
        print("\n")

    elif option=="3":
        nome=input("Qual nome deseja remover? ")
        db_delete(nome)
        print("\n",nome,"removido(a) da agenda com sucesso\n") 

    elif option=="4":
        nome= input("Qual usuário deseja alterar? ")
        mail=input("Qual o novo email? ")
        db_update(nome,mail)
        print("\n Contato Alterado\n") 

    elif option=="5":
        report=db_select_all()
        print("\n Relatório Gerado:")
        print ("{:<5} {:<8} {:<10} {:<14} {:<8} {:<8}".format('ID','Nome','Telefone','E-mail','Twitter','Instagram'))
        pprint(report)
        print("\n")
        

    elif option=="6":
        print("\n Até Logo \n")
        break 

    else:
        print("\n Opção inválida, escolha outra opção\n") 