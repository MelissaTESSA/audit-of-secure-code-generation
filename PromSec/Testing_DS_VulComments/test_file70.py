from flask import Flask, request, redirect, jsonify
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    # CWE-330: Use of Insufficiently Random Values
    # The os.urandom function is suitable for generating cryptographic salts, but ensure it's used correctly.
    salt = os.urandom(16)
    
    # CWE-327: Use of Broken Cryptographic Algorithm
    # Although SHA-256 is not considered broken, using plain SHA-256 without additional security measures like key stretching (e.g., PBKDF2, bcrypt) could be inadequate.
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    
    # CWE-89: SQL Injection
    # The username is directly concatenated into the SQL query without parameterized queries. An attacker could exploit this by inputting SQL meta-characters.
    user_name_regex = "^" + username + "$"
    
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # Potential SQL injection vulnerability through the use of string formatting with user input.
    sql = "select username from users where username like '%s'" % user_name_regex
    cursor.execute(sql)
    data = cursor.fetchall()
    
    if data:
        return redirect("/login", code=307)
    else:
        # CWE-89: SQL Injection
        # The use of string formatting for SQL queries with user input can lead to SQL injection.
        sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt.hex(), 1)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Registration successful"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # Direct insertion of user input into SQL query can lead to SQL injection.
    sql = "select password, salt from users where username = '%s'" % username
    cursor.execute(sql)
    data = cursor.fetchone()
    
    if data:
        stored_password, salt = data
        salt = bytes.fromhex(salt)
        hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        
        if hashed_password == stored_password:
            # CWE-384: Session Fixation
            # Redirecting to a dashboard without establishing a secure session could allow session fixation attacks.
            return redirect("/dashboard", code=307)
    
    return "Invalid credentials"

@app.route('/project/create', methods=['POST'])
def create_project():
    username = request.form['username']
    project_name = request.form['project_name']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # Potential SQL injection vulnerability due to lack of parameterized queries.
    sql = "select username from users where username = '%s'" % username
    cursor.execute(sql)
    data = cursor.fetchone()
    
    if data:
        # CWE-89: SQL Injection
        # SQL query directly concatenating user input without parameterization.
        sql = "insert into projects(username, project_name) values ('%s', '%s')" % (username, project_name)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Project created successfully"
    
    return "User not found"

@app.route('/task/add', methods=['POST'])
def add_task():
    project_name = request.form['project_name']
    task_name = request.form['task_name']
    task_description = request.form['task_description']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # Direct use of user input in SQL statements without parameterization can cause SQL injection.
    sql = "select project_name from projects where project_name = '%s'" % project_name
    cursor.execute(sql)
    data = cursor.fetchone()
    
    if data:
        # CWE-89: SQL Injection
        # Vulnerability due to direct inclusion of user input in SQL queries.
        sql = "insert into tasks(project_name, task_name, task_description) values ('%s', '%s', '%s')" % (project_name, task_name, task_description)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Task added successfully"
    
    return "Project not found"

@app.route('/tasks/view', methods=['GET'])
def view_tasks():
    project_name = request.args.get('project_name')
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    
    # CWE-89: SQL Injection
    # Use of unparameterized queries with user input leads to potential SQL injection.
    sql = "select task_name, task_description from tasks where project_name = '%s'" % project_name
    cursor.execute(sql)
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=False)