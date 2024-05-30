'''
Module 5 SQL Project
Author: Kari Taylor
Objective: Create a Python script that demonstrates the ability to interact with a SQL database, including creating a database, defining a schema, and executing various SQL commands. Incorporate logging to document the process and provide user feedback.
'''

# Import Standard Dependencies
import csv
import pathlib
import sqlite3
import uuid
import logging

# Import Local Dependencies
import pandas as pd
import pyarrow

# Define database file in the root project folder
db_file = pathlib.Path("project.db")

# Define function to insert records from a CSV
def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

# Define function for inserting new records to the data tables
def execute_insert_records(db_file, insert_records_sql_file):
    with sqlite3.connect(db_file) as conn:
        insert_records_sql_file = pathlib.Path("insert_records.sql")
        with open(insert_records_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {insert_records_sql_file}")

# Define function for deleting records from the data tables
def execute_delete_records(db_file, delete_records_sql_file):
    with sqlite3.connect(db_file) as conn:
        delete_records_sql_file = pathlib.Path("delete_records.sql")
        with open(delete_records_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {delete_records_sql_file}")

# Define function for updating records from the data tables
def execute_update_records(db_file, update_records_sql_file):
    with sqlite3.connect(db_file) as conn:
        update_records_sql_file = pathlib.Path("update_records.sql")
        with open(update_records_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {update_records_sql_file}")

# Define function for performing operations on data from tables
def execute_query_aggregation(db_file, query_aggregation_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_aggregation_sql_file = pathlib.Path("query_aggregation.sql")
        with open(query_aggregation_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_aggregation_sql_file}")

# Define function for filtering data from tables
def execute_query_filter(db_file, query_filter_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_filter_sql_file = pathlib.Path("query_filter.sql")
        with open(query_filter_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_filter_sql_file}")

# Define function for grouping data from tables
def execute_query_group_by(db_file, query_group_by_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_group_by_sql_file = pathlib.Path("query_group_by.sql")
        with open(query_group_by_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_group_by_sql_file}")

# Define function for combining data from 2 tables
def execute_query_join(db_file, query_join_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_join_sql_file = pathlib.Path("query_join.sql")
        with open(query_join_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_join_sql_file}")

# Define function for sorting data in tables
def execute_query_sorting(db_file, query_sorting_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_sorting_sql_file = pathlib.Path("query_sorting.sql")
        with open(query_sorting_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_sorting_sql_file}")


def main():

    # Create database schema and populate with data
    execute_insert_records(db_file, 'insert_records.sql')
    execute_delete_records(db_file, 'delete_records.sql')
    execute_update_records(db_file, 'update_records.sql')
    execute_query_aggregation(db_file, 'query_aggregation.sql')
    execute_query_filter(db_file, 'query_filter.sql')
    execute_query_group_by(db_file, 'query_group_by.sql')
    execute_query_join(db_file, 'query_join.sql')
    execute_query_sorting(db_file, 'query_sorting.sql')

    logging.info("All SQL operations completed successfully")

    

if __name__ == "__main__":
    logging.info("Program started") # add this at the beginning of the main method
    main()
    logging.info("Program ended")  # add this at the end of the main method


   