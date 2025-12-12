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
    cur.execute("SELECT password FROM user_info WHERE username=%s", [username])
    row = cur.fetchone()
    if (row[0] == hashlib.md5(password.encode("utf-8")).hexdigest()):
        return redirect('/')
    else:
        return redirect('/error')