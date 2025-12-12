from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

#log in the user if the username and password are correct
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()
    cur.execute("SELECT id, username, password, accesslevel FROM user WHERE username='" + username + "'")
    result = cur.fetchone()
    if result:
        #hash the password and compare it to what is in the database, if it is correct log the user in
        pwdHash = hashlib.md5()
        pwdHash.update(password)
        pwdTest = pwdHash.hexdigest()
        if pwdTest != result[2]:
            return "Incorrect Password"
        else:
            return redirect('/user', code=302)
    else:
        return "User does not exist"

"""
-----Examples-----
Input:
An HTTP POST request with form data containing 'username' and 'password'
login()
Output:
Redirect to '/user' if credentials are correct, otherwise return "Incorrect Password" or "User does not exist"
"""