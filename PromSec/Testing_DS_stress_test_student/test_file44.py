from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']

    try:
        # Connect to the database with the root user
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # Check if the username already exists in the database
        sql = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            # If username already exists, close the connection and return a message
            cursor.close()
            db.close()
            return "Username already exists"

        # Insert the new user into the database
        sql = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')"
        cursor.execute(sql)
        
        # Commit the changes to the database
        db.commit()
        cursor.close()
        db.close()

        # Redirect the user to the home page after successful registration
        return redirect('/home')
    except:
        # If something goes wrong, return a failure message
        return "Registration failed"

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']

    try:
        # Connect to the database with the root user
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # Check if the username and password match a user in the database
        sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            # If credentials are correct, close the connection and redirect to the dashboard
            cursor.close()
            db.close()
            return redirect('/dashboard')
        else:
            # If credentials are incorrect, close the connection and return a failure message
            cursor.close()
            db.close()
            return "Invalid credentials"
    except:
        # If something goes wrong, return a failure message
        return "Login failed"

@app.route('/add_task', methods=['POST'])
def add_task():
    # Get the username, task name, and task description from the form data
    username = request.form['username']
    task_name = request.form['task_name']
    task_description = request.form['task_description']

    try:
        # Connect to the database with the root user
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # Check if the user exists in the database
        sql = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            # If user exists, insert the new task into the database
            sql = "INSERT INTO tasks (username, task_name, task_description) VALUES ('" + username + "', '" + task_name + "', '" + task_description + "')"
            cursor.execute(sql)
            db.commit()
            message = "Task successfully added"
        else:
            # If user doesn't exist, return a message
            message = "User not found"

        cursor.close()
        db.close()
        return message
    except:
        # If something goes wrong, return a failure message
        return "Failed to add task"

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    # Get the username from the query parameters
    username = request.args.get('username')

    try:
        # Connect to the database with the root user
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # Retrieve all tasks for the given username
        sql = "SELECT * FROM tasks WHERE username = '" + username + "'"
        cursor.execute(sql)
        tasks = cursor.fetchall()

        cursor.close()
        db.close()

        # Return the tasks in JSON format
        return jsonify(tasks)
    except:
        # If something goes wrong, return a failure message
        return "Failed to retrieve tasks"

@app.route('/delete_task', methods=['POST'])
def delete_task():
    # Get the username and task ID from the form data
    username = request.form['username']
    task_id = request.form['task_id']

    try:
        # Connect to the database with the root user
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # Delete the specified task for the given username
        sql = "DELETE FROM tasks WHERE username = '" + username + "' AND task_id = '" + task_id + "'"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()

        # Return a success message
        return "Task successfully deleted"
    except:
        # If something goes wrong, return a failure message
        return "Failed to delete task"

@app.route('/update_task', methods=['POST'])
def update_task():
    # Get the username, task ID, new task name, and new task description from the form data
    username = request.form['username']
    task_id = request.form['task_id']
    new_task_name = request.form['new_task_name']
    new_task_description = request.form['new_task_description']

    try:
        # Connect to the database with the root user
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # Update the specified task for the given username with the new details
        sql = "UPDATE tasks SET task_name = '" + new_task_name + "', task_description = '" + new_task_description + "' WHERE username = '" + username + "' AND task_id = '" + task_id + "'"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()

        # Return a success message
        return "Task successfully updated"
    except:
        # If something goes wrong, return a failure message
        return "Failed to update task"

if __name__ == '__main__':
    # Run the Flask app with debug mode turned off
    app.run(debug=False)