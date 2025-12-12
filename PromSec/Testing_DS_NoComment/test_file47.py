from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])

def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username='" + username + "'")
    results = cursor.fetchall()
    if len(results) == 0:
        return "Login failed!"
    hashed_password = results[0][1]
    if hashed_password == hashlib.sha1(password).hexdigest():
        return "Welcome " + username + "!"
    else:
        return "Login failed!"