import os
from flask import Flask, request, jsonify
import mysql.connector
import hashlib
import uuid

app = Flask(__name__)

db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

def generate_salt():
    return uuid.uuid4().hex

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def check_user_existence(username):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    return True if result else False

def register_user(username, password):
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)", (username, hashed_password, salt))
    db.commit()
    cursor.close()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if check_user_existence(username):
        return jsonify({'error': 'Username already exists'}), 400

    register_user(username, password)
    return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
    app.run()