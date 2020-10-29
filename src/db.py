""" Database methods
"""

import sqlite3

def create_connection():
    """ Connect to database and return a database cursor object
    """
    conn = None
    try:
        conn = sqlite3.connect('messages.db')
        c = conn.cursor()
        return (c, conn)
    except Exception as e:
        print(e)
    return conn

def delete_database():
    """ Delete all tables
    """
    # connect to database
    c, conn = create_connection()
    c.execute('DROP TABLE participants')
    c.execute('DROP TABLE messages')
    conn.commit()
    conn.close()

def create_tables():
    c, conn = create_connection()

    # delete tables from previous session
    delete_database()


    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS participants
                (name text)''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS messages
        (sender_name text, content text, timestamp_ms integer, type text)
    ''')


def insert_to_database(data):
    """ Given a dict object representing messages from facebook,
    upload messages and participants into table
    """
    # connect to database
    c, conn = create_connection()

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


def test():
    # connect to database
    c, conn = create_connection()
    # c.execute("SELECT * FROM participants")
    # c.execute("SELECT COUNT(content) from messages")
    c.execute("SELECT DISTINCT type from messages")
    

    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

