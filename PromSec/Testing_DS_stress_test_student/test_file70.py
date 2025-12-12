from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Get username and password from the form
    username = request.form['username']
    password = request.form['password']
    # Generate a random salt for password hashing
    salt = os.urandom(16)
    # Combine salt and password, then hash them for storage
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    # Create a regex pattern to check username
    user_name_regex = "^" + username + "$"
    # Connect to the database
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    # Check if the username already exists
    sql = "select username from users where username like '%s'" % user_name_regex
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        # If username exists, redirect to login
        return redirect("/login", code=307)
    else:
        # If username doesn't exist, insert the new user into the database
        sql = "insert into users(username, password, salt, account_created) values ('%s','%s', '%s', %d)" % (username, hashed_password, salt.hex(), 1)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Registration successful"

@app.route('/login', methods=['POST'])
def login():
    # Get username and password from the form
    username = request.form['username']
    password = request.form['password']
    # Connect to the database
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    # Retrieve stored password and salt for the username
    sql = "select password, salt from users where username = '%s'" % username
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        stored_password, salt = data
        salt = bytes.fromhex(salt)
        # Hash the provided password with the stored salt
        hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        # Check if the hashed password matches the stored password
        if hashed_password == stored_password:
            return redirect("/dashboard", code=307)
    return "Invalid credentials"

@app.route('/project/create', methods=['POST'])
def create_project():
    # Get username and project name from the form
    username = request.form['username']
    project_name = request.form['project_name']
    # Connect to the database
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    # Check if the user exists
    sql = "select username from users where username = '%s'" % username
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        # Insert the new project into the database
        sql = "insert into projects(username, project_name) values ('%s', '%s')" % (username, project_name)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Project created successfully"
    return "User not found"

@app.route('/task/add', methods=['POST'])
def add_task():
    # Get project name, task name, and task description from the form
    project_name = request.form['project_name']
    task_name = request.form['task_name']
    task_description = request.form['task_description']
    # Connect to the database
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    # Check if the project exists
    sql = "select project_name from projects where project_name = '%s'" % project_name
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        # Insert the new task into the database
        sql = "insert into tasks(project_name, task_name, task_description) values ('%s', '%s', '%s')" % (project_name, task_name, task_description)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return "Task added successfully"
    return "Project not found"

@app.route('/tasks/view', methods=['GET'])
def view_tasks():
    # Get project name from the query parameters
    project_name = request.args.get('project_name')
    # Connect to the database
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    # Get all tasks for the specified project
    sql = "select task_name, task_description from tasks where project_name = '%s'" % project_name
    cursor.execute(sql)
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(tasks)

if __name__ == '__main__':
    # Run the app in debug mode to see errors and reload automatically
    app.run(debug=False)