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
   salt = os.urandom(16)

def register():
   username = request.form['username']
   password = request.form['password']
   salt = os.urandom(16)
   m = hashlib.sha256()
   m.update(password.encode('utf-8') + salt)
   password = m.digest() + salt
   print(password)
   try:
      db = MySQLdb.connect("localhost","root","cisco123","mysite")
      cursor = db.cursor()
      sql = "insert into user (username,password) values ('"+username+"','"+password+"')"
      print(sql)
      cursor.execute(sql)
      cursor.execute("commit")
      return redirect('/home')
   except:
      return redirect('/home')