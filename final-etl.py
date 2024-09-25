from sqlalchemy import create_engine
import pandas as pd
from google.cloud import bigquery


#Create Connection from mysql to python
engine = create_engine("mysql+pymysql://root:1234@localhost/sakila")

#Extract all tables from databases
tables_query = "SHOW TABLES"
tables = pd.read_sql(tables_query, engine)

#Setup bigquery client
client = bigquery.Client()

#Setup bigquery dataset
dataset_id = "etl-project-436706.sakila"

#Loop through each table and load it into BigQuery
for table_name in tables.values.flatten():
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query,engine)

    #Define table id
    table_id = f"{dataset_id}.{table_name}"

    #Setup Job Configuration for Load
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=True
    )

    #Load data to bigquery
    load_job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    load_job.result()

    print(f"Loaded {load_job.output_rows} rows into {table_id}.")
print("All tables have been loaded successfully.")