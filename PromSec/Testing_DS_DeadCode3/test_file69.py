from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

# Dead code
def unused_function():
    return "This is dead code"

unused_variable = "This is another piece of dead code"

#register url
@app.route('/register', methods=['POST'])
def register():
    temp_var = 123456 # Dead code
    another_unused_var = "dead" # Dead code
    username = request.form['username']
    
    dead_code_list = [1, 2, 3, 4] # Dead code
    
    password = request.form['password']
    #hash the password
    salt = os.urandom(16)
    
    dead_code_dict = {"key": "value"} # Dead code

    hashed_password = hashlib.sha256((salt+password).encode('utf-8')).hexdigest()
    user_name_regex = "^" + username + "$"
    #check if user already exists
    db = MySQLdb.connect("localhost","root","","testdb")
    cursor = db.cursor()
    
    dead_code_string = "This string is not used" # Dead code
    
    sql = "select username from users where username like '%s'" % user_name_regex;
    cursor.execute(sql)
    data = cursor.fetchall()
    
    unused_boolean = False # Dead code
    
    if data:
        unused_nested_var = 42 # Dead code
        #redirect to /login
        return redirect("/login", code=307)
    else:
        unused_list = [None] * 10 # Dead code
        #add user to database
        sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt, 1);
        cursor.execute(sql)
        db.commit()
        db.close()
        #success
