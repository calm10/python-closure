"""
Module contains dao of first name table
"""
from typing import List
from src.dao.database_connector import get_database_connection

def insert_data(items: List[tuple]):
    """
    It inserts data into the first name table
    Args:
        items: table data

    Returns:
        None
    """
    print("Insert entry in first_name table")
    query = "INSERT into first_name (id, name) VALUES (%s, %s)"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.executemany(query, items)
    connector.commit()

def drop_table():
    """
    It drops the table

    """
    print("Drop first_name table")
    query = "DROP table first_name"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.execute(query)
    connector.commit()

def create_table():
    """
    It creates table first_name which id as primary key and name as other column
    """
    print("Create first_name table")
    query = "CREATE TABLE first_name (id INT(11) NOT NULL PRIMARY KEY, name VARCHAR(255))"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.execute(query)
    connector.commit()
