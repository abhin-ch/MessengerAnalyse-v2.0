""" Database methods
"""

import sqlite3

def create_connection(db_name=None):
    """ Connect to database and return a database cursor object
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        return (c, conn)
    except Exception as e:
        print(e)
    return conn


def delete_database(db_name=None):
    """ Delete all tables
    """
    c, conn = create_connection(db_name)
    c.execute('DROP TABLE IF EXISTS participants')
    c.execute('DROP TABLE IF EXISTS messages')
    conn.commit()
    conn.close()


def create_tables(db_name=None):
    c, conn = create_connection(db_name)
    # Create tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS participants
        (name text)''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS messages
        (sender_name text, content text, timestamp_ms integer, type text)
    ''')
    conn.commit()
    conn.close()


def insert_to_database(db_name, data):
    """ Given a dict object representing messages from facebook,
    upload messages and participants into table
    """
    c, conn = create_connection(db_name)
    row = []
    keys = ['name']
    for content in data['participants']:
        [row.append(content[k]) if k in content else row.append(None) for k in keys]
        c.execute("INSERT INTO participants VALUES (?)", row)
        row = []

    row = []
    keys = ["sender_name", "content", "timestamp_ms", "type"]
    for content in data['messages']:
        [row.append(content[k]) if k in content else row.append(None) for k in keys]

        # Insert a row of data
        c.execute("INSERT INTO messages VALUES (?, ?, ?, ?)", row)
        row = []

    # save changes and close connection
    conn.commit()
    conn.close()


def _init(db_name, data):
    """ Delete tables from previous session, and create new tables
    """
    delete_database(db_name) # delete tables from previous session
    create_tables(db_name) # create new tables
    insert_to_database(db_name, data) # insert json into database

class DataGateway:
    """ Acts as a gateway for a database. One instance handles all
    transactions and database operations
    """
    def __init__(self, db_name):
        # connect to database, where database is name
        self.db_name = db_name

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            return (c, conn)
        except Exception as e:
            print(e)
        return conn

    
    def _execute(self, query, commit=False):
        # perform the given query on the db object
        # if the query requires to be commited to be saved
        # set commit = True
        data = None
        c, conn = self.create_connection()
        c.execute(query)
        if commit:
            conn.commit()
        else:
            data = c.fetchall()
        conn.close()
        return data
        

    def select(self, query):
        # return the result of a select statement as a tuple
        return self._execute(query)

 
if __name__ == "__main__":
    db = DataGateway('messages.db')
    data = db.select('SELECT *, 0 from participants')
    print({k:v for k,v in data})
    # print(data)



# def test():
#     # connect to database
#     c, conn = create_connection('messages.db')
#     # c.execute("SELECT * FROM participants")
#     # c.execute("SELECT COUNT(content) from messages")
#     c.execute("SELECT DISTINCT type from messages")
    

#     rows = c.fetchall()
#     for row in rows:
#         print(row)
#     conn.close()

