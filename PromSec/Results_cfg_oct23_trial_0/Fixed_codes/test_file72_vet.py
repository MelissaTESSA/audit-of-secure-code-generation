import os
from flask import Flask, request, redirect
import hashlib
import mysql.connector

app = Flask(__name__)

def connect_to_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user (username, key, salt) VALUES (%s, %s, %s)", (username, key, salt))
        conn.commit()
        return redirect('/home')
    except mysql.connector.Error:
        conn.rollback()
        return redirect('/home')

if __name__ == '__main__':
    app.run()