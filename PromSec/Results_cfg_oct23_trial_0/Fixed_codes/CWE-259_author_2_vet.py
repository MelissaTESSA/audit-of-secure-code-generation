import mysql.connector
import os

def getConnection():
    """
    This function returns a secure connection object for a MySQL database.

    Example:
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name")
    result = cursor.fetchall()
    conn.close()

    Returns:
    MySQL connection object
    """
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB")
    )
    
    return conn