import os
import mysql.connector

def get_user_info(username):
    """
    Connects to a MySQL database and retrieves user information based on the username provided.

    Input:
    username (str): The username of the user to retrieve information for.

    Output:
    user_info (dict): A dictionary containing the user information retrieved from the database.
    """

    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    cnx = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = cnx.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user_info = cursor.fetchone()

    cursor.close()
    cnx.close()

    return user_info