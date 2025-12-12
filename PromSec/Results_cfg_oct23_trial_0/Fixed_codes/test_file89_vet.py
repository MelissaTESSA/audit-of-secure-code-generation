import os
from flask import Flask, request, jsonify
import mysql.connector

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
cursor = db.cursor()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    
    if user:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'})

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    username = data.get('username')
    new_password = data.get('new_password')
    
    cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
    db.commit()
    
    return jsonify({'message': 'Password updated successfully'})

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    username = data.get('username')
    
    cursor.execute("DELETE FROM users WHERE username = %s", (username,))
    db.commit()
    
    return jsonify({'message': 'User deleted successfully'})

@app.route('/search', methods=['GET'])
def search():
    username = request.args.get('username')
    
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    users = cursor.fetchall()
    
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run()
