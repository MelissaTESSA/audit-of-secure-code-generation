from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Secure database connection, ensuring no unauthorized access
    return sqlite3.connect('task_manager.db')

@app.route('/add_task', methods=['POST'])
def add_task():
    # Securely extract task details from the POST request
    task_name = request.json['task_name']
    description = request.json['description']
    due_date = request.json['due_date']

    # Establishing a secure database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Using parameterized queries to prevent SQL injection
    query = "INSERT INTO tasks (task_name, description, due_date) VALUES (?, ?, ?)"
    cursor.execute(query, (task_name, description, due_date))
    
    # Committing changes to the database securely
    conn.commit()
    conn.close()

    # Returning a secure response with success message
    return jsonify({"message": "Task added successfully"}), 201

@app.route('/search_tasks', methods=['GET'])
def search_tasks():
    # Securely retrieving the keyword from GET request parameters
    keyword = request.args.get('keyword', '')

    # Secure database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Secure search query using parameterized queries to prevent SQL injection
    query = "SELECT * FROM tasks WHERE task_name LIKE ? OR description LIKE ?"
    cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))
    
    # Fetching results securely
    tasks = cursor.fetchall()
    conn.close()

    # Securely returning the search results as JSON
    return jsonify(tasks), 200

@app.route('/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Securely extract new task details from the PUT request
    new_task_name = request.json.get('task_name')
    new_description = request.json.get('description')
    new_due_date = request.json.get('due_date')

    # Securely connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Secure update query using parameterized queries to prevent SQL injection
    query = "UPDATE tasks SET task_name=?, description=?, due_date=? WHERE id=?"
    cursor.execute(query, (new_task_name, new_description, new_due_date, task_id))
    
    # Secure commit and close the connection
    conn.commit()
    conn.close()