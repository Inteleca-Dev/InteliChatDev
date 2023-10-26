'''
This file handles all the database related operations.
'''
import pyodbc
class Database:
    def __init__(self):
        # Connect to the database
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=server_name;'
                                   'Database=db_name;'
                                   'Trusted_Connection=yes;')
    def fetch_data(self, user_id):
        # Fetch data for the user
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM table_name WHERE user_id = ?', user_id)
        return cursor.fetchall()