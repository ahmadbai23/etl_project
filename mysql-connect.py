from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://root:1234@localhost/sakila")

query = "SELECT * FROM actor"

df = pd.read_sql(query,engine)
print(df.head())