import os
import mysql.connector

def get_user_data(username):
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
    user_data = cursor.fetchone()

    cursor.close()
    conn.close()

    return user_data

# Example usage
username = 'john_doe'
user_data = get_user_data(username)
print(user_data)