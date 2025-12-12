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

        db = MySQLdb.connect(host="localhost",user="root",passwd="r0cknr0l",db="cwe200")
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            usernamecwe200 = row[0]
            passwordhashcwe200 = row[2]

        if (password == passwordhashcwe200):
            return redirect("/cwe200/" + usernamecwe200)
        else:
            return redirect("/cwe200/")
    except MySQLdb.Error as e:
        print ("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)
    finally:
        db.close()