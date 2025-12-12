import os
from flask import Flask, request
import hashlib
import mysql.connector

app = Flask(__name__)

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = db.cursor()

def generate_salt():
    return os.urandom(16).hex()

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def user_exists(username):
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    return result is not None

def register_user(username, password):
    if user_exists(username):
        return "User already exists"

    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    query = "INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, hashed_password, salt))
    db.commit()

    return "User registered successfully"

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "Username and password are required"

    result = register_user(username, password)
    return result

if __name__ == '__main__':
    app.run()