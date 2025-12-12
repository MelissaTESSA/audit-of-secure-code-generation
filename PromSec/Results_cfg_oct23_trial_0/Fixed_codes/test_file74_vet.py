from flask import Flask, request, redirect
import bcrypt
import MySQLdb
import os

app = Flask(__name__)

def connect_db():
    return MySQLdb.connect(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), database=os.getenv("DB_NAME"))

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if not username or not password or not confirm_password:
        return "Missing username, password, or confirm_password", 400

    if password != confirm_password:
        return "Passwords do not match", 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        db.close()
        return "Username already exists", 400

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    db.commit()
    db.close()

    return "Registration successful"

if __name__ == '__main__':
    app.run()
