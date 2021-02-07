"""
Module contains dao of last name table
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
    print("Insert entry in last_name table")
    query = "INSERT into last_name (id, name) VALUES (%s, %s)"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.executemany(query, items)
    connector.commit()


def drop_table():
    """
    It drops the table

    """
    print("Drop last_name table")
    query = "DROP table last_name"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.execute(query)
    connector.commit()


def create_table():
    """
    It creates table last_name which id as primary key and name as other column

    """
    print("Create last_name table")
    query = "CREATE TABLE last_name (id INT(11) NOT NULL PRIMARY KEY, name VARCHAR(255))"
    connector = get_database_connection()
    cursor = connector.cursor()
    cursor.execute(query)
    connector.commit()
