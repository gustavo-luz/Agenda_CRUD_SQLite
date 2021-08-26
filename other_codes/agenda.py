from DML import db_insert,db_select,db_update,db_delete
from pprint import pprint

#name,phone,email,twitter,facebook)
db_insert('caio','99999999','caio@gmail.com','cai','caiai')
db_insert('jose','99999999','jos@gmail.com','jojo','jsoiai')
db_insert('andre','99999999','anda@gmail.com','adnsn','and')

#dados e campo
#pprint(db_select('id','3'))

#TODO fix sqlite3.OperationalError: no such column: Gustavo
#pprint(db_select("twitter","cai"))