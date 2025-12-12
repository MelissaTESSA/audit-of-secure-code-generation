import os
import mysql.connector

def connect_to_mysql():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    return conn

# Example usage
# connection = connect_to_mysql()
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM table_name")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)