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

# Import Local Dependencies
#import pandas as pd
#import pyarrow


import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def main():
    create_database()

if __name__ == "__main__":
    main()
