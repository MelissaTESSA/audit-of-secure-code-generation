import os
import mysql.connector

def get_user_info(username):
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

    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user_info = cursor.fetchone()

    cursor.close()
    conn.close()

    return user_info

# Example usage
username = 'john_doe'
user_info = get_user_info(username)
print(user_info)