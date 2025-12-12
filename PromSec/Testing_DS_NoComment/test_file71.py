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
   encrypted_password = hashlib.sha1(password + salt).hexdigest()
   conn = MySQLdb.connect(host= "localhost",
                           user="Raju",
                           passwd="raju",
                           db="CWE")
   x = conn.cursor()
   sql = "INSERT INTO users (username, password, salt, created_at, updated_at) VALUES ( '{}','{}','{}',NOW(),NOW())".format(username, encrypted_password, salt)
   x.execute(sql)
   conn.commit()