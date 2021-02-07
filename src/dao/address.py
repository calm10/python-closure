"""
Module contains dao of address table
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
    print("Insert entry in address table")
    query = "INSERT into address (id, name) VALUES (%s, %s)"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.executemany(query, items)
    connector.commit()

def drop_table():
    """
    It drops the table

    """
    print("Drop address table")
    query = "DROP table address"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.execute(query)
    connector.commit()


def create_table():
    """
    It creates table address which id as primary key and name as other column

    """
    print("Create address table")
    query = "CREATE TABLE address (id INT(11) NOT NULL PRIMARY KEY, name VARCHAR(255))"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.execute(query)
    connector.commit()
