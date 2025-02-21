from utils.schema_sql import TODO_SCHEMA
import sqlite3

# DB Name
DB_NAME = 'todoDB.db'


# @create_connection
# @brief: Create a connection to the database
# @return: Connection object as conn and Cursor
def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        return conn, conn.cursor()
    except Exception as e:
        print("Error Form database Connection: ", e)
        return None


# @db_initialize
# @brief: Initialize the database  by executing schema.sql
# @return: Void
def db_initialize():
    conn, cursor = create_connection()
    cursor.execute(TODO_SCHEMA)
    conn.commit()
    conn.close()
