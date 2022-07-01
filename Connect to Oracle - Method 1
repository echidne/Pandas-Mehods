import pandas as pd
import cx_Oracle
import credentials # a simple module where you pur your credentials in

#initiation Oracle Client (only necessary when working on Windows and when your database is not on your machine)
cx_Oracle.init_oracle_client(lib_dir=r"C:\.....\Oracle\instantclient_21_3")

#create credentials variable
username = credentials.username
password = credentials.password
host = credentials.host
port = credentials.port
DatabaseName = credentials.DatabaseName

#query
query = """
select ....
from ....
where ....
"""

#connection to the database
oracl_connect = cx_Oracle(username, password, f"{host}:{port}/{DatabaseName}")

#create a dataframe
df= pd.read_sql(query, con = oracl_connect)

#close connection if connection
if oracl_connect:
  oracl_connect.close()
