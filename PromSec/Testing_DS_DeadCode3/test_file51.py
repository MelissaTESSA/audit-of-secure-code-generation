#copilot mean_prob: 0.5795225243675477
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

# Dead code block 1
unused_var_1 = "This is unused code block 1"

#log in the user if the username and password are correct
@app.route('/login', methods=['POST'])

# Dead code block 2
unused_var_2 = "This is unused code block 2"

def login():
    # Dead code block 3
    unused_var_3 = "This is unused code block 3"
    
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()
    
    # Dead code block 4
    unused_var_4 = "This is unused code block 4"
    
    cur.execute("SELECT id, username, password, accesslevel FROM user WHERE username='" + username + "'")
    result = cur.fetchone()
    
    # Dead code block 5
    unused_var_5 = "This is unused code block 5"
    
    if result:
        #hash the password and compare it to what is in the database, if it is correct log the user in
        pwdHash = hashlib.md5()
        pwdHash.update(password)
        
        # Dead code block 6
        unused_var_6 = "This is unused code block 6"
        
        pwdTest = pwdHash.hexdigest()
        if pwdTest != result[2]:
            
            # Dead code block 7
            unused_var_7 = "This is unused code block 7"
            
            return "Incorrect Password"
        else:
            return redirect('/user', code=302)
    else:
        # Dead code block 8
        unused_var_8 = "This is unused code block 8"
        
        return "User does not exist"

# Dead code block 9
unused_var_9 = "This is unused code block 9"

# Dead code block 10
unused_var_10 = "This is unused code block 10"
