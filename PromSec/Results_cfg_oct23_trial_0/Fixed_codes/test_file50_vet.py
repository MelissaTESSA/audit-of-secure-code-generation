import os
from flask import Flask, request
import mysql.connector
import hashlib

app = Flask(__name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def connect_to_database():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )

def check_login(username, password):
    hashed_password = hash_password(password)
    db = connect_to_database()
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, hashed_password))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result is not None

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if check_login(username, password):
        return 'Login successful'
    else:
        return 'Login failed'

if __name__ == '__main__':
    app.run()