import os
import mysql.connector

def get_user_info(username):
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user_info = cursor.fetchall()

    for user in user_info:
        print(user)

    cursor.close()
    conn.close()

get_user_info('example_user')