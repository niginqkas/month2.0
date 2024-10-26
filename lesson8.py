import sqlite3


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        print(error)
        return connection


db_name = '''hw_db'''
my_connection = create_connection(db_name)
if my_connection is not None:
    print('Connected to database')
    my_connection.close()




