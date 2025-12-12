import os
from flask import Flask, request
import hashlib
import mysql.connector

app = Flask(__name__)

db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'root')
db_name = os.getenv('DB_NAME', 'db')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def db_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    hashed_password = hash_password(password)

    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM userdaten WHERE username = %s AND password = %s"
    cursor.execute(query, (username, hashed_password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return "Eingeloggt"
    else:
        return "Falscher Benutzername oder Passwort"

if __name__ == '__main__':
    app.run()