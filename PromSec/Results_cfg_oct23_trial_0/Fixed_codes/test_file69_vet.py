import os
from flask import Flask, request
import mysql.connector
import hashlib
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASS'),
    database=os.environ.get('DB_NAME')
)

def generate_salt():
    return os.urandom(16)

def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)", (username, hashed_password, salt))
    db.commit()
    
    return 'User registered successfully'

if __name__ == '__main__':
    app.run()