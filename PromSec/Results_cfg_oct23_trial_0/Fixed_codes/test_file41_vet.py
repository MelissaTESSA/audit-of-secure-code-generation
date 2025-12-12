import os
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_NAME = os.getenv('DB_NAME', 'cwe_900')

def db_connect():
    return mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME)

def register_user(username, password):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone() is not None:
            return "Username already exists"
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return "You have successfully registered"
    except Exception as e:
        print(e)
        return "Registration Failed"
    finally:
        cursor.close()
        conn.close()

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return "Invalid input"
    result = register_user(username, password)
    return result

if __name__ == '__main__':
    app.run()
