import os
import mysql.connector

def get_database_credentials():
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    return db_host, db_user, db_password, db_name

def establish_database_connection():
    db_host, db_user, db_password, db_name = get_database_credentials()
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    return conn

# Example usage
connection = establish_database_connection()
print(connection)