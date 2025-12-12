import os
import mysql.connector

def get_user_info(username):
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user_info = cursor.fetchone()

        cursor.close()
        connection.close()

        return user_info

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

username = 'example_user'
user_info = get_user_info(username)
print(user_info)