import os
import mysql.connector

def connect_to_mysql():
    db_host = os.getenv("DB_HOST", "localhost")
    db_user = os.getenv("DB_USER", "root")
    db_password = os.getenv("DB_PASSWORD", "mysecretpassword")
    db_name = os.getenv("DB_NAME", "mydatabase")
    
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

# Usage
db_connection = connect_to_mysql()
print(db_connection)