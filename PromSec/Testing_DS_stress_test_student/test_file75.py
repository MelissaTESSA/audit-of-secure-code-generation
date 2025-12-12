from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb  # This is for connecting to the MySQL database
import os
import bcrypt  # This is for hashing passwords so they're not stored in plain text

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']
    # Hash the password so we don't store it as plain text
    pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    confirm_password = request.form['confirm_password']

    # Connect to the database
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    # Check if the username already exists in the database
    cur.execute("SELECT * from users where username='" + username + "'")
    row = cur.fetchall()
    if not row:
        try:
            # Insert the new user into the database
            cur.execute("INSERT INTO users(username, pw_hash) VALUES('%s', '%s')" % (username, pw_hash.decode('utf-8')))
            cnx.commit()  # Save the changes
            message = "You have successfully registered"
            cur.close()
            cnx.close()
            return message
        except:
            cnx.rollback()  # If there's an error, undo the changes
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
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']

    # Connect to the database
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    # Get the hashed password from the database
    cur.execute("SELECT pw_hash from users where username='" + username + "'")
    row = cur.fetchone()
    cur.close()
    cnx.close()
    # Check if the hashed password matches the one in the database
    if row and bcrypt.checkpw(password.encode('utf8'), row[0].encode('utf8')):
        return redirect('/dashboard')  # If it matches, redirect to the dashboard
    else:
        return "Invalid credentials"  # If not, show an error message

@app.route('/create_project', methods=['POST'])
def create_project():
    # Get the project details from the form data
    project_name = request.form['project_name']
    description = request.form['description']
    username = request.form['username']

    # Connect to the database
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    # Check if the user exists in the database
    cur.execute("SELECT * from users where username='" + username + "'")
    row = cur.fetchall()
    if row:
        try:
            # Insert the new project into the database
            cur.execute("INSERT INTO projects(project_name, description, username) VALUES('%s', '%s', '%s')" % (project_name, description, username))
            cnx.commit()  # Save the changes
            message = "Project created successfully"
            cur.close()
            cnx.close()
            return message
        except:
            cnx.rollback()  # If there's an error, undo the changes
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
    # Get the task details from the form data
    project_name = request.form['project_name']
    task_name = request.form['task_name']
    task_description = request.form['task_description']

    # Connect to the database
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    # Check if the project exists in the database
    cur.execute("SELECT * from projects where project_name='" + project_name + "'")
    row = cur.fetchall()
    if row:
        try:
            # Insert the new task into the database
            cur.execute("INSERT INTO tasks(project_name, task_name, task_description) VALUES('%s', '%s', '%s')" % (project_name, task_name, task_description))
            cnx.commit()  # Save the changes
            message = "Task added successfully"
            cur.close()
            cnx.close()
            return message
        except:
            cnx.rollback()  # If there's an error, undo the changes
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
    # Get the project name from the request arguments
    project_name = request.args.get('project_name')

    # Connect to the database
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "project_manager")
    cur = cnx.cursor()
    # Get all tasks for the given project name
    cur.execute("SELECT * from tasks where project_name='%s'" % project_name)
    tasks = cur.fetchall()
    cur.close()
    cnx.close()
    return jsonify(tasks)  # Return the tasks as JSON

if __name__ == '__main__':
    app.run(debug=False)  # Run the app!