from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():

    username = request.form['username']
    password = request.form['password']

    # Securely generate a cryptographically secure random salt
    salt = os.urandom(16)

    # Use SHA-1 hashing algorithm combined with salt for secure password storage
    encrypted_password = hashlib.sha1(password + salt).hexdigest()

    # Establish a secure connection to the database with appropriate credentials
    conn = MySQLdb.connect(host="localhost",
                           user="Raju",
                           passwd="raju",
                           db="CWE")
    x = conn.cursor()

    # Use parameterized queries to prevent SQL injection
    sql = "INSERT INTO users (username, password, salt, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
    x.execute(sql, (username, encrypted_password, salt))

    # Commit the transaction securely
    conn.commit()