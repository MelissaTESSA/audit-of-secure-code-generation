import os
import hashlib
import binascii
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

def generate_salt():
    return os.urandom(16)

def hash_password(password, salt):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return binascii.hexlify(key)

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    
    cnx = mysql.connector.connect(user='root', password=os.environ.get('MYSQL_ROOT_PASSWORD'),
                                  host='localhost', database='CWE')
    cursor = cnx.cursor()
    
    add_user = ("INSERT INTO users "
                "(username, password, salt, created_at) "
                "VALUES (%s, %s, %s, NOW())")
    user_data = (username, hashed_password, salt)
    cursor.execute(add_user, user_data)
    
    cnx.commit()
    cursor.close()
    cnx.close()
    
    return 'User registered successfully'

if __name__ == '__main__':
    app.run()