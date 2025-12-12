from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])

def register():
   username = request.form['username']
   password = request.form['password']
   password = hashlib.md5(password).hexdigest()
   db = MySQLdb.connect(host="69.195.55.111", user= "ec2-user", passwd="ufo12345", db="CWE")
   cur = db.cursor()
   query ="INSERT INTO User (Username, Password, Email) VALUES ('%s', '%s', '%s')" % (username, password, username)
   cur.execute(query)
   db.commit()
   db.close()

   return redirect('/')