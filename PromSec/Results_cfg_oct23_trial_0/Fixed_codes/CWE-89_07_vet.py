import sqlite3
import os

def fetch_user_details(username, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    result = cursor.fetchone()
    
    conn.close()
    
    return f'User details fetched successfully for {username}.'

username = "johndoe"
db_path = "./Test/CWE-89_07/test_db.sqlite"
fetch_user_details(username, db_path)