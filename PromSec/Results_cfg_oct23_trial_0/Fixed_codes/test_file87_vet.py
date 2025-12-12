import os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'])
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'})

@app.route('/update_profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    username = data['username']
    new_password = generate_password_hash(data['new_password'])
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Profile updated successfully'})

@app.route('/search_users', methods=['GET'])
def search_users():
    query = request.args.get('query')
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username LIKE %s", ('%' + query + '%',))
    users = cur.fetchall()
    cur.close()
    
    return jsonify({'users': users})

@app.route('/delete_account', methods=['DELETE'])
def delete_account():
    data = request.get_json()
    username = data['username']
    
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE username = %s", (username,))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Account deleted successfully'})

if __name__ == '__main__':
    app.run()
