"""
Module contains connector of mysql database
"""
from mysql.connector import connect, Error

def get_database_connection(database="test"):
    """
    It creates connection to local database
    Args:
        database: database

    Returns:
        connection object
    """
    # put host, user and password details in config with encrypted data
    try:
        return connect(host='localhost',
                       user='user',
                       password='password',
                       database=database)
    except Error as err:
        print(err)

def get_all_tables():
    """
    Query database to get all the tables
    Returns:
        list of tables
    """
    connector = get_database_connection()
    query = "SHOW tables"
    cursor = connector.cursor()
    cursor.execute(query)
    return cursor.fetchall()
