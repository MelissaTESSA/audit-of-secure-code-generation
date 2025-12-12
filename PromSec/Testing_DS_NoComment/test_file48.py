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
    c = db.cursor()
    c.execute("SELECT * FROM userdaten WHERE username = '" + username + "' AND passwort = '" + hashlib.md5(password).hexdigest() + "'")
    if c.fetchone():
        return "Eingeloggt"
    else:
        return "Falscher Benutzername oder Passwort"