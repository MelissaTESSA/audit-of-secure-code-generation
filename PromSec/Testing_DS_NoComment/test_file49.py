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
    cur.execute("SELECT * FROM users WHERE username='" + username + "' AND pass='" + password + "'")
    result = cur.fetchone()

    if(result == None):
        return redirect('/')
    else:
        return redirect('/dashboard')