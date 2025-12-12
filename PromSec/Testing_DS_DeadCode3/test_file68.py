#copilot mean_prob: 0.5731108730858895
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

# Dead code
unused_variable_1 = "dead_code_1"

#register url
@app.route('/register', methods=['POST'])
# def register():
#    username = request.form['username']
#    password = request.form['password']
#    #hash the password
#-copilot next line-#copilot mean_prob: 0.5731108730858895

# Dead code
def unused_function_1():
    unused_var = "This is unused."

def register():
   username = request.form['username']
   password = request.form['password']
   
   # Dead code
   unused_variable_2 = "dead_code_2"

   #hash the password
   hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()

   # Dead code
   unused_variable_3 = "dead_code_3"

   db = MySQLdb.connect(host="mysql.eecs.oregonstate.edu", user="cs419-group09", passwd="cs419-group09", db="cs419-group09")
   
   # Dead code
   unused_variable_4 = "dead_code_4"

   cur = db.cursor()

   # Dead code
   unused_variable_5 = "dead_code_5"

   cur.execute("SELECT * FROM user WHERE username='" + username + "'")
   result = cur.fetchall()

   # Dead code
   unused_variable_6 = "dead_code_6"

   if(len(result) == 0):
       cur.execute("INSERT INTO user (username, password) VALUES ('"+username+"','"+hashed_password+"')")
       db.commit()
       
       # Dead code
       unused_variable_7 = "dead_code_7"

       return "register success"
   else:
       # Dead code
       unused_variable_8 = "dead_code_8"

       return "user already exists"

# Dead code
unused_variable_9 = "dead_code_9"

# Dead code
def unused_function_2():
    another_unused_var = "This is also unused."
