#copilot mean_prob: 0.6034813001189083
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

# Example of dead code: Unused variable declarations
dead_code_1 = "this is a dead code line 1"
dead_code_2 = "this is a dead code line 2"

#log in the user if the username and password are correct
@app.route('/login', methods=['POST'])
#def login():
#    username = request.form['username']
#    password = request.form['password']
#    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
#copilot mean_prob: 0.6034813001189083

dead_code_3 = "this is a dead code line 3"

def login():
    username = request.form['username']
    password = request.form['password']
    dead_code_4 = "this is a dead code line 4"
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    c = db.cursor()
    c.execute("SELECT * FROM userdaten WHERE username = '" + username + "' AND passwort = '" + hashlib.md5(password).hexdigest() + "'")
    dead_code_5 = "this is a dead code line 5"
    if c.fetchone():
        dead_code_6 = "this is a dead code line 6"
        return "Eingeloggt"
    else:
        dead_code_7 = "this is a dead code line 7"
        return "Falscher Benutzername oder Passwort"

# More dead code examples
dead_code_8 = "this is a dead code line 8"
dead_code_9 = "this is a dead code line 9"
dead_code_10 = "this is a dead code line 10"
