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
    query = "SELECT * FROM user WHERE username='%s' AND password='%s'" % (username, password)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    db.close()
    if len(results) == 0:
        return "Bad Login"
    else:
        return "Good Login"