from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    try:
        # CWE-798: Use of Hard-coded Credentials
        # Hardcoded database credentials are used, which can expose the database to unauthorized access if the code is leaked.
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # CWE-89: SQL Injection
        # User input 'username' is directly concatenated into the SQL query string, allowing for SQL injection attacks.
        # Example payload: username = "'; DROP TABLE users; --"
        sql = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            cursor.close()
            db.close()
            return "Username already exists"

        # CWE-89: SQL Injection
        # Both 'username' and 'password' are directly concatenated into the SQL query string, allowing for SQL injection.
        # Example payload: username = "'; DROP TABLE users; --", password = "any"
        sql = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')"
        cursor.execute(sql)
        
        db.commit()
        cursor.close()
        db.close()

        return redirect('/home')
    except:
        # CWE-209: Information Exposure Through Error Messages
        # Generic error message does not provide details, but catching all exceptions without logging can hide issues.
        return "Registration failed"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # CWE-89: SQL Injection
        # User inputs 'username' and 'password' are directly concatenated, allowing for SQL injection attacks.
        # Example payload: username = "' OR '1'='1", password = "' OR '1'='1"
        sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            cursor.close()
            db.close()
            return redirect('/dashboard')
        else:
            cursor.close()
            db.close()
            return "Invalid credentials"
    except:
        return "Login failed"

@app.route('/add_task', methods=['POST'])
def add_task():
    username = request.form['username']
    task_name = request.form['task_name']
    task_description = request.form['task_description']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # CWE-89: SQL Injection
        # User input 'username' is directly concatenated into the SQL query string, allowing for SQL injection.
        sql = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            # CWE-89: SQL Injection
            # User inputs 'username', 'task_name', and 'task_description' are concatenated, allowing for SQL injection.
            sql = "INSERT INTO tasks (username, task_name, task_description) VALUES ('" + username + "', '" + task_name + "', '" + task_description + "')"
            cursor.execute(sql)
            db.commit()
            message = "Task successfully added"
        else:
            message = "User not found"

        cursor.close()
        db.close()
        return message
    except:
        return "Failed to add task"

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    username = request.args.get('username')

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # CWE-89: SQL Injection
        # User input 'username' is directly concatenated into the SQL query string, allowing for SQL injection.
        sql = "SELECT * FROM tasks WHERE username = '" + username + "'"
        cursor.execute(sql)
        tasks = cursor.fetchall()

        cursor.close()
        db.close()

        # CWE-200: Information Exposure
        # Returning raw database output could expose sensitive information.
        return jsonify(tasks)
    except:
        return "Failed to retrieve tasks"

@app.route('/delete_task', methods=['POST'])
def delete_task():
    username = request.form['username']
    task_id = request.form['task_id']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # CWE-89: SQL Injection
        # User inputs 'username' and 'task_id' are directly concatenated into the SQL query string, allowing for SQL injection.
        sql = "DELETE FROM tasks WHERE username = '" + username + "' AND task_id = '" + task_id + "'"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()

        return "Task successfully deleted"
    except:
        return "Failed to delete task"

@app.route('/update_task', methods=['POST'])
def update_task():
    username = request.form['username']
    task_id = request.form['task_id']
    new_task_name = request.form['new_task_name']
    new_task_description = request.form['new_task_description']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        # CWE-89: SQL Injection
        # User inputs 'username', 'task_id', 'new_task_name', and 'new_task_description' are directly concatenated, allowing for SQL injection.
        sql = "UPDATE tasks SET task_name = '" + new_task_name + "', task_description = '" + new_task_description + "' WHERE username = '" + username + "' AND task_id = '" + task_id + "'"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()

        return "Task successfully updated"
    except:
        return "Failed to update task"

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Running the application with 'debug=False' is correct for production, but ensure no debug code remains.
    app.run(debug=False)