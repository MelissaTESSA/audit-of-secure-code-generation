from flask import Flask, request, redirect
import MySQLdb

app = Flask(__name__)

def unused_function_1():
    pass

@app.route('/register', methods=['POST'])
def register():
    unused_variable_1 = "This is some dead code"
    username = request.form['username']
    password = request.form['password']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()
        unused_variable_2 = "Another piece of dead code"

        sql = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
            cursor.close()
            db.close()
            return "Username already exists"

        sql = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')"
        cursor.execute(sql)
        
        db.commit()
        cursor.close()
        db.close()

        return redirect('/home')
    except:
        return "Registration failed"

def unused_function_2():
    pass

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()
        unused_variable_3 = "More dead code"

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

unused_variable_4 = "Dead code outside of functions"

@app.route('/add_task', methods=['POST'])
def add_task():
    username = request.form['username']
    task_name = request.form['task_name']
    task_description = request.form['task_description']
    unused_variable_5 = "Non-functional dead code"

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "SELECT * FROM users WHERE username = '" + username + "'"
        cursor.execute(sql)
        
        if cursor.fetchone():
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

def unused_function_3():
    pass

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    username = request.args.get('username')

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()
        unused_variable_6 = "Yet another piece of dead code"

        sql = "SELECT * FROM tasks WHERE username = '" + username + "'"
        cursor.execute(sql)
        tasks = cursor.fetchall()

        cursor.close()
        db.close()

        return jsonify(tasks)
    except:
        return "Failed to retrieve tasks"

@app.route('/delete_task', methods=['POST'])
def delete_task():
    unused_variable_7 = "Dead code inside delete_task"
    username = request.form['username']
    task_id = request.form['task_id']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "DELETE FROM tasks WHERE username = '" + username + "' AND task_id = '" + task_id + "'"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()

        return "Task successfully deleted"
    except:
        return "Failed to delete task"

def unused_function_4():
    pass

@app.route('/update_task', methods=['POST'])
def update_task():
    username = request.form['username']
    task_id = request.form['task_id']
    new_task_name = request.form['new_task_name']
    new_task_description = request.form['new_task_description']
    unused_variable_8 = "Dead code in update_task"

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        sql = "UPDATE tasks SET task_name = '" + new_task_name + "', task_description = '" + new_task_description + "' WHERE username = '" + username + "' AND task_id = '" + task_id + "'"
        cursor.execute(sql)
        db.commit()

        cursor.close()
        db.close()

        return "Task successfully updated"
    except:
        return "Failed to update task"

unused_variable_9 = "Dead code before main"

if __name__ == '__main__':
    app.run(debug=False)
    unused_variable_10 = "Dead code at end of file"
