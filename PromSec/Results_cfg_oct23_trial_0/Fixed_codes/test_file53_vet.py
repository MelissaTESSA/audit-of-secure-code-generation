import os
from flask import Flask, request, jsonify
import hashlib
import mysql.connector

app = Flask(__name)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def verify_credentials(username, password):
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    name = os.environ.get('DB_NAME')

    conn = mysql.connector.connect(user=user, password=password, host=host, database=name)
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, hashed_password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return True
    else:
        return False

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if verify_credentials(username, password):
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})

if __name__ == '__main__':
    app.run()