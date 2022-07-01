import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import config_db

#initiation Oracle Client (only if on Windows and distant database)
cx_Oracle.init_oracle_client(lib_dir=r"C:\......\Oracle\instantclient_21_3")

#import config_db
username = config_db.username
password = config_db.password
host = config_db.host
port = config_db.port
DatabaseName = config_db.DatabaseName

#Query
query= """
select ....
from ....
where ....
"""

#creation of SQL engine
oracle_connection_string = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/{DatabaseName}'
engine = create_engine(oracle_connection_string)

#function to request oracle DB Solution
def read_solution(query, engine):
    try:
        data= pd.read_sql(query, engine)
    except BaseException as e:
        print(e)
    return data
