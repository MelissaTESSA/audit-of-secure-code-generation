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
   hashed_password = hashlib.sha256((salt+password).encode('utf-8')).hexdigest()
   user_name_regex = "^" + username + "$"
   db = MySQLdb.connect("localhost","root","","testdb")
   cursor = db.cursor()
   sql = "select username from users where username like '%s'" % user_name_regex;
   cursor.execute(sql)
   data = cursor.fetchall()
   if data:
      return redirect("/login", code=307)
   else:
      sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt, 1);
      cursor.execute(sql)
      db.commit()
      db.close()