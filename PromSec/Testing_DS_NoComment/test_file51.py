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
    cur = db.cursor()
    cur.execute("SELECT id, username, password, accesslevel FROM user WHERE username='" + username + "'")
    result = cur.fetchone()
    if result:
        pwdHash = hashlib.md5()
        pwdHash.update(password)
        pwdTest = pwdHash.hexdigest()
        if pwdTest != result[2]:
            return "Incorrect Password"
        else:
            return redirect('/user', code=302)
    else:
        return "User does not exist"