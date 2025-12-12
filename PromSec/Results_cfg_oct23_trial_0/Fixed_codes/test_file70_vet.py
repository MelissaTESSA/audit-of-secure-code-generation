import os
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    mysql.connection.commit()

    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if not user or not bcrypt.check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful'})

@app.route('/create_project', methods=['POST'])
def create_project():
    data = request.get_json()
    project_name = data.get('project_name')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO projects (project_name) VALUES (%s)", (project_name,))
    mysql.connection.commit()

    return jsonify({'message': 'Project created successfully'})

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    project_id = data.get('project_id')
    task_name = data.get('task_name')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tasks (project_id, task_name) VALUES (%s, %s)", (project_id, task_name))
    mysql.connection.commit()

    return jsonify({'message': 'Task added successfully'})

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    project_id = request.args.get('project_id')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks WHERE project_id = %s", (project_id,))
    tasks = cur.fetchall()

    if not tasks:
        return jsonify({'message': 'No tasks found for this project'}), 404

    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run()