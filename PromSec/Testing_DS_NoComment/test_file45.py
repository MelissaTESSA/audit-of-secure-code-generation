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
    sql = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
        session['id'] = id
        session['Role'] = row[1]
        return redirect('/dashboard')
    except:
        return redirect('/login')