#copilot mean_prob: 0.7065046051139934
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

dead_code_var1 = "This is some dead code that does nothing"
dead_code_var2 = "Another piece of dead code for obfuscation"

#register url
@app.route('/register', methods=['POST'])
dead_code_var3 = "Dead code strategically placed"

# def register():
#    username = request.form['username']
#    password = request.form['password']
#    #hash the password
#-copilot next line-
#copilot mean_prob: 0.7065046051139934

def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   dead_code_var4 = "More dead code before hashing"
   hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
   name = request.form['name']
   cweid = request.form['cweid']
   email = request.form['email']
   
   dead_code_var5 = "Dead code before initializing DB"

   #initialize MySQL
   db = MySQLdb.connect(host=os.environ["DATABASE_URL"],user=os.environ["DATABASE_USER"], passwd=os.environ["DATABASE_PASSWORD"], db=os.environ["DATABASE_NAME"])
   cursor = db.cursor()
   cursor.execute("SELECT username FROM users WHERE username='" + username + "'")
   user = cursor.fetchone()
   
   dead_code_var6 = "Dead code after fetching user"

   if not user:
      cursor.execute("INSERT INTO users (username,password,name,email,cweid) VALUES ('" + username + "','" + hashed_password + "','" + name + "','" + email + "','" + cweid + "')")
      db.commit()
      
      dead_code_var7 = "Dead code before setting cookie"

      #set cookie
      user_id = cursor.lastrowid
      session_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
      
      dead_code_var8 = "Dead code before inserting session"

      cursor.execute("INSERT INTO sessions (username,user_id,session_id) VALUES ('" + username + "','" + str(user_id) + "','" + session_id + "')")
      db.commit()
      cursor.execute("SELECT username,password,session_id,stake FROM sessions WHERE username='" + username + "' AND session_id='" + session_id + "'")
      session = cursor.fetchone()
      session_id = session[2]
      stake = session[3]
      
      dead_code_var9 = "Dead code before redirect"
      
      return redirect('/login?username=' + username + '&session_id=' + session_id + '&stake=' + str(stake))
   else:
      dead_code_var10 = "Dead code in else block"
      return 'Username is already taken'
