from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://root:1234@localhost/sakila")

tables_query = "SHOW TABLES"
tables = pd.read_sql(tables_query,engine)

table_name=[]
for table in tables.values.flatten():
    table_name.append(table)

print(table_name)