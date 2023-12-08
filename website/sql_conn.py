from urllib import parse
import pyodbc
from sqlalchemy import create_engine
import urllib

SQL_QUERY = 'SELECT name FROM master.dbo.sysdatabases'
SERVER = 'DESKTOP-VOE2SHH'
DATABASE = 'Website'

USERNAME = 'Mithun_sql'
PASSWORD = 'password123'
PORT = '1433'

import pyodbc
import sqlserverport
# servername = 'DESKTOP-VOE2SHH'
# serverspec = '{0},{1}'.format(
#     servername,
#     sqlserverport.lookup(servername, 'MSSQLSERVER'))
# print(serverspec)
connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};PORT={PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
# conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER={};...'.format(serverspec))
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(r)


# params = parse.quote_plus \
# (r'Driver={ODBC Driver 17 for SQL Server};Server=tcp:DESKTOP-VOE2SHH,1433;Database=BikeStores;Uid=Mithun_sql;Pwd={password123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

# conn_str="mssql+pyodbc:///?odbc_connect={}".format(params)
# conn_str="mssql+pyodbc://Mithun_sql:password123@DESKTOP-VOE2SHH/Website?driver=SQL+Server"


# engine= create_engine (conn_str,echo=True)

# from sqlalchemy import text
# query1 = 'create database Website'

# connection = engine.connect()
# result1 = connection.execute(text(query1))

# # print(result)
# query2 = 'SELECT name FROM master.dbo.sysdatabases'

# result2 = connection.execute(text(query2))


# for row in result2:
#     print(row)

# connection.close()

#to make pyodbc work in linux
# $ sudo apt install unixodbc
