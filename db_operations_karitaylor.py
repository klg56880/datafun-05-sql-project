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
db_file = "C:\\Users\\klg56\\OneDrive\\Documents\\datafun-05-sql-project\\project.db"

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

def main():
    insert_data_from_csv()

if __name__ == "__main__":
    logging.info("Program started") # add this at the beginning of the main method
    main()
    logging.info("Program ended")  # add this at the end of the main method

# Define function for inserting new records to the data tables
def insert_records():