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
    cursor.execute("SELECT password FROM user WHERE username = '" + username + "'")
    login_results = cursor.fetchall()
    db.close()
    if login_results == ():
        return "Wrong Password"
    for row in login_results:
        if row[0] == hashlib.md5(password.encode()).hexdigest():
            print(row[0])
            return "Login Success"
    return "Wrong Username"