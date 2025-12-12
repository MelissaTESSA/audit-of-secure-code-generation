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
    try:

        conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="cwe200")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"'")
        rows = cursor.fetchall()
        if len(rows) > 0:
            session['username'] = username
            return redirect('/session')
        else:
            return 'Incorrect username or password'
    except MySQLdb.Error:
        return 'Incorrect username or password'