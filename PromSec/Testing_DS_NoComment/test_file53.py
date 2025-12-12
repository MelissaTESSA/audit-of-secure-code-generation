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
    query = "SELECT * FROM user WHERE username = '" + str(username) + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    db.close()
    for row in rows:
       if row[1] == username:
           if row[2] == hashlib.md5(password.encode()).hexdigest():
               return "success"
           else:
               return "wrong pw"
    return "username not found"