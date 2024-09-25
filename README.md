# MySQL to BigQuery Data Transfer Project

## Description
This project aims to transfer data from a MySQL database to Google BigQuery using Python. It is designed to simplify the data migration process, enabling faster and more efficient analysis in BigQuery.

## Code Usage Order
1. **`mysql-connect.py`**: Establishes a connection from MySQL to Python.
2. **`looping-all-tables.py`**: Checks all tables in the database.
3. **`bigquery-connect.py`**: Ensures a connection to Google BigQuery.
4. **`final-etl.py`**: Contains the final code for the entire ETL process.

## Resources
- **Folder: `bahan`**: Contains resources used in this project.
- **Folder: `sakila csv`**: A collection of CSV files for individual uploads.
- **Folder: `sakila sql`**: Contains SQL syntax for inserting data into the local MySQL database.

## Features
- Connect and retrieve data from the MySQL database.
- Convert data to the appropriate format for BigQuery.
- Batch transfer data to Google BigQuery.
- Provide logging to monitor the status of the data transfer.

## Technologies
- **Python**: The programming language used for developing the scripts.
- **SQLAlchemy**: Used to connect and interact with the MySQL database.
- **Google Cloud BigQuery**: The data storage service used for data analysis.
- **pandas**: Used for data manipulation and conversion.


