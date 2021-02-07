"""
Module contains three table join
"""
import time
from src.dao.database_connector import get_database_connection, get_all_tables
from src.dao.first_name import drop_table as drop_first_name, \
    create_table as create_first_name, insert_data as insert_first_name
from src.dao.last_name import drop_table as drop_last_name, \
    create_table as create_last_name, insert_data as insert_last_name
from src.dao.address import drop_table as drop_address, \
    create_table as create_address, insert_data as insert_address

def three_table_result(table1="first_name",
                       table2="last_name",
                       table3="address"):

    def _insert_data(count):
        """
        It inserts data into tables
        Args:
            count: number of items needs to inserted

        """
        name = ['a', 'b', 'cc', 'd', 'e', 'f', 'i', 'j', 'k', 'h']
        items = []
        for i in range(0, count):
            item = (i, name[i % 10])
            items.append(item)

        insert_first_name(items)
        insert_last_name(items)
        insert_address(items)

    def _create_all_tables():
        """
        It creates tables first_name, last_name and address
        """
        create_first_name()
        create_last_name()
        create_address()

    def _drop_all_tables():
        """
        It drops all the table
        """
        tables = get_all_tables()
        for table in tables:
            print(table)
            if table[0] == table1:
                drop_first_name()
            elif table[0] == table2:
                drop_last_name()
            elif table[0] == table3:
                drop_address()
            else:
                pass

    def _get_three_table_join_time():
        """
        It joins three table and sends the response time taken by the query
        Returns:
            response time
        """
        start_time = time.time()
        query = "Select * from first_name join last_name on first_name.id = last_name.id " \
                "join address on address.id = first_name.id"
        db = get_database_connection()
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            pass
        end_time = time.time()
        return (end_time - start_time) * 1000

    def result(count=1000):
        """
        It drops table if exists, creates new one and insert data,
        and measures time taken by the join query
        Returns:
            time taken in milliseconds
        """
        _drop_all_tables()
        _create_all_tables()
        _insert_data(count)
        time_taken = _get_three_table_join_time()
        return time_taken
    return result
