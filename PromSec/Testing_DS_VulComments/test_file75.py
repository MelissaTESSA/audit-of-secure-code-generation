from flask import Flask, request, redirect, jsonify
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    confirm_password = request.form['confirm_password']

    # CWE-798: Use of Hard-coded Credentials
    # The database connection uses hard-coded credentials, which can be easily exploited if the code is exposed.
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    
    # CWE-89: SQL Injection
    # The username is directly concatenated into the SQL query, allowing an attacker to inject SQL code.
    cur.execute("SELECT * from users where username='" + username + "'")
    row = cur.fetchall()
    
    if not row:
        try:
            # CWE-89: SQL Injection
            # The username and pw_hash are formatted directly into the SQL query, allowing SQL injection.
            cur.execute("INSERT INTO users(username, pw_hash) VALUES('%s', '%s')" % (username, pw_hash.decode('utf-8')))
            cnx.commit()
            message = "You have successfully registered"
            cur.close()
            cnx.close()
            return message
        except:
            # CWE-209: Information Exposure Through Error Messages
            # Generic error message, but specific rollback details might be logged elsewhere, potentially exposing sensitive information.
            cnx.rollback()
            message = "Registration Failed"
            cur.close()
            cnx.close()
            return message
    else:
        message = "Username already exists"
        cur.close()
        cnx.close()
        return message

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # CWE-798: Use of Hard-coded Credentials
    # The database connection uses hard-coded credentials, which can be easily exploited if the code is exposed.
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    
    # CWE-89: SQL Injection
    # The username is directly concatenated into the SQL query, allowing an attacker to inject SQL code.
    cur.execute("SELECT pw_hash from users where username='" + username + "'")
    row = cur.fetchone()
    cur.close()
    cnx.close()
    
    if row and bcrypt.checkpw(password.encode('utf8'), row[0].encode('utf8')):
        # CWE-601: Open Redirect
        # The redirect location is hardcoded here, but if it were based on user input, it could lead to open redirect vulnerabilities.
        return redirect('/dashboard')
    else:
        return "Invalid credentials"

@app.route('/create_project', methods=['POST'])
def create_project():
    project_name = request.form['project_name']
    description = request.form['description']
    username = request.form['username']

    # CWE-798: Use of Hard-coded Credentials
    # The database connection uses hard-coded credentials, which can be easily exploited if the code is exposed.
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    
    # CWE-89: SQL Injection
    # The username is directly concatenated into the SQL query, allowing an attacker to inject SQL code.
    cur.execute("SELECT * from users where username='" + username + "'")
    row = cur.fetchall()
    
    if row:
        try:
            # CWE-89: SQL Injection
            # The project_name, description, and username are formatted directly into the SQL query, allowing SQL injection.
            cur.execute("INSERT INTO projects(project_name, description, username) VALUES('%s', '%s', '%s')" % (project_name, description, username))
            cnx.commit()
            message = "Project created successfully"
            cur.close()
            cnx.close()
            return message
        except:
            # CWE-209: Information Exposure Through Error Messages
            # Generic error message, but specific rollback details might be logged elsewhere, potentially exposing sensitive information.
            cnx.rollback()
            message = "Project creation failed"
            cur.close()
            cnx.close()
            return message
    else:
        message = "User not found"
        cur.close()
        cnx.close()
        return message

@app.route('/add_task', methods=['POST'])
def add_task():
    project_name = request.form['project_name']
    task_name = request.form['task_name']
    task_description = request.form['task_description']

    # CWE-798: Use of Hard-coded Credentials
    # The database connection uses hard-coded credentials, which can be easily exploited if the code is exposed.
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    
    # CWE-89: SQL Injection
    # The project_name is directly concatenated into the SQL query, allowing an attacker to inject SQL code.
    cur.execute("SELECT * from projects where project_name='" + project_name + "'")
    row = cur.fetchall()
    
    if row:
        try:
            # CWE-89: SQL Injection
            # The project_name, task_name, and task_description are formatted directly into the SQL query, allowing SQL injection.
            cur.execute("INSERT INTO tasks(project_name, task_name, task_description) VALUES('%s', '%s', '%s')" % (project_name, task_name, task_description))
            cnx.commit()
            message = "Task added successfully"
            cur.close()
            cnx.close()
            return message
        except:
            # CWE-209: Information Exposure Through Error Messages
            # Generic error message, but specific rollback details might be logged elsewhere, potentially exposing sensitive information.
            cnx.rollback()
            message = "Task addition failed"
            cur.close()
            cnx.close()
            return message
    else:
        message = "Project not found"
        cur.close()
        cnx.close()
        return message

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    project_name = request.args.get('project_name')

    # CWE-798: Use of Hard-coded Credentials
    # The database connection uses hard-coded credentials, which can be easily exploited if the code is exposed.
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    
    # CWE-89: SQL Injection
    # The project_name is formatted directly into the SQL query, allowing SQL injection.
    cur.execute("SELECT * from tasks where project_name='%s'" % project_name)
    tasks = cur.fetchall()
    cur.close()
    cnx.close()
    
    # CWE-200: Information Exposure
    # Returning raw database output as JSON without filtering could expose sensitive internal data.
    return jsonify(tasks)

if __name__ == '__main__':
    # CWE-16: Configuration
    # Application running with debug=False is good, but ensure other configurations (like allowed hosts) are secure.
    app.run(debug=False)