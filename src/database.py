import sqlite3

# DB Name
DB_NAME = 'todoDB.db'

# @create_connection
# @brief: Create a connection to the database
# @return: Connection object as conn and Cursor


def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        conn.row_factory = sqlite3.Row  # Allows column access by name
        return conn, conn.cursor()
    except Exception as e:
        print("Error Form database Connection: ", e)
        return None


# @db_initialize
# @brief: Initialize the database  by executing schema.sql
# @return: Void
def db_initialize():
    conn, cursor = create_connection()
    # Executes all SQL commands in schema.sql
    with open('./utils/schema.sql', "r") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()
