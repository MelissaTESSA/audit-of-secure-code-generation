from flask import Flask, request, redirect, jsonify
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Securely retrieve the username and password from the form data
    username = request.form['username']
    password = request.form['password']
    
    # Generate a secure hash of the password using bcrypt
    pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    confirm_password = request.form['confirm_password']

    # Securely connect to the database
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()

    # Use parameterized queries to prevent SQL injection
    cur.execute("SELECT * from users where username=%s", (username,))
    row = cur.fetchall()
    if not row:
        try:
            # Insert the new user into the database securely
            cur.execute("INSERT INTO users(username, pw_hash) VALUES(%s, %s)", (username, pw_hash.decode('utf-8')))
            cnx.commit()
            message = "You have successfully registered"
            cur.close()
            cnx.close()
            return message
        except:
            # Rollback transaction in case of any error to maintain database integrity
            cnx.rollback()
            message = "Registration Failed"
            cur.close()
            cnx.close()
            return message
    else:
        message = "Username already exists"
        cur.close()
        cnx.close()
        return message

@app.route('/login', methods=['POST'])
def login():
    # Securely retrieve the username and password from the form data
    username = request.form['username']
    password = request.form['password']

    # Securely connect to the database
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()

    # Use parameterized queries to prevent SQL injection
    cur.execute("SELECT pw_hash from users where username=%s", (username,))
    row = cur.fetchone()
    cur.close()
    cnx.close()
    
    # Securely verify the password using bcrypt
    if row and bcrypt.checkpw(password.encode('utf8'), row[0].encode('utf8')):
        return redirect('/dashboard')
    else:
        return "