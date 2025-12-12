import os
from flask import Flask, request, redirect, make_response
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
bcrypt = Bcrypt()

host = os.environ.get('DB_HOST')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DB_NAME')

db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = db.cursor()

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    email = request.form.get('email')
    cweid = request.form.get('cweid')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone() is not None:
        return 'Username is already taken'

    cursor.execute("INSERT INTO users (username, password, name, email, cweid) VALUES (%s, %s, %s, %s, %s)",
                   (username, hashed_password, name, email, cweid))
    db.commit()

    session_id = os.urandom(16).hex()
    response = make_response(redirect('/login'))
    response.set_cookie('session_id', session_id)
    response.set_cookie('username', username)
    response.set_cookie('stake', '100')
    
    return response

if __name__ == '__main__':
    app.run()
