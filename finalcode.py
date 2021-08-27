
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

#update
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

    option=True

while option:
    
    print ("""
    Menu:\n
    1. Inserir Contato
    2. Consultar Contato
    3. Remover Contato
    4. Alterar Contato
    5. Gerar Relatório
    6. Criar Tabela no SQLite
    7. Excluir Tabela no SQLite
    8. Sair
    """)
    option=input("Escolha uma opção do Menu: ")


    if option=="1":
        print("\nOpção 1. Inserir Contato\n")
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
        print("\nOpção 2. Consultar Contato\n")
        nome=input("Qual nome deseja encontrar? ")
        consulta=(db_select(nome))
        print("\n Retorno da Busca:")
        print ("{:<5} {:<8} {:<10} {:<14} {:<8} {:<8}".format('ID','Nome','Telefone','E-mail','Twitter','Instagram'))
        pprint(consulta) 
        print("\n")

    elif option=="3":
        print("\nOpção 3. Remover Contato\n")
        nome=input("\n Qual nome deseja remover? \n")
        db_delete(nome)
        print("\n",nome,"removido(a) da agenda com sucesso\n") 

    elif option=="4":
        print("\nOpção 4. Alterar Contato\n")
        nome= input("\nQual usuário deseja alterar?\n ")
        mail=input("\nQual o novo email?\n ")
        db_update(nome,mail)
        print("\n Contato Alterado\n") 

    elif option=="5":
        print("\nOpção 5. Gerar Relatório\n")
        report=db_select_all()
        print("\n Relatório Gerado:\n")
        print ("{:<5} {:<8} {:<10} {:<14} {:<8} {:<8}".format('ID','Nome','Telefone','E-mail','Twitter','Instagram'))
        pprint(report)
        print("\n")
    
    elif option=="6":
        print("\nOpção 6. Criar Tabela no SQLite\n")
        report=db_creation()
        print("\n Tabela criada \n")

    elif option=="7":
        print("\nOpção 7. Excluir Tabela no SQLite\n")
        report=db_drop()
        print("\n Tabela exluida \n")

    elif option=="8":
        print("\nOpção 8. Sair\n")
        print("\n Até Logo \n")
        break 

    else:
        print("\n Opção inválida, escolha outra opção\n") 