
import pandas as pd
import MySQLdb as mdb
from sqlalchemy import create_engine
from datetime import datetime

source = mdb.connect('localhost','root','12345','bdjeff_backup')
# destination = mdb.connect('localhost','root','12345','test_panda_restore')
destination = create_engine("mysql+mysqldb://root:12345@localhost/test_panda_restore")

tables = pd.read_sql('show tables', source)

def read_data(table):
    source_table_rows = pd.read_sql('select * from {0}' .format(table), source)
    source_table_rows.to_sql(name='{0}' .format(table), con=destination, if_exists='replace', index=True)

start = datetime.now()

# print type(tables)
tables['Tables_in_bdjeff_backup'].apply(read_data)

stop = datetime.now()

print '\nTotal time taken: ', stop - start, '\n'
