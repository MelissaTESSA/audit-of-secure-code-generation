from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('task_manager.db')

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.json['task_name']
    description = request.json['description']
    due_date = request.json['due_date']

    # CWE-89: SQL Injection
    # Vulnerability: The SQL query is constructed using string concatenation with user input. 
    # User input: task_name, description, due_date
    # Impact: An attacker could execute arbitrary SQL commands, leading to data leakage, modification, or destruction.
    # Example attack payload: task_name = "task1'); DROP TABLE tasks;--"
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO tasks (task_name, description, due_date) VALUES ('{task_name}', '{description}', '{due_date}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully"}), 201

@app.route('/search_tasks', methods=['GET'])
def search_tasks():
    keyword = request.args.get('keyword', '')

    # CWE-89: SQL Injection
    # Vulnerability: The SQL query is constructed using string concatenation with user input.
    # User input: keyword
    # Impact: An attacker could execute arbitrary SQL commands, leading to data leakage, modification, or destruction.
    # Example attack payload: keyword = "test' OR '1'='1"
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM tasks WHERE task_name LIKE '%{keyword}%' OR description LIKE '%{keyword}%'"
    cursor.execute(query)
    
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200

@app.route('/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task_name = request.json.get('task_name')
    new_description = request.json.get('description')
    new_due_date = request.json.get('due_date')

    # CWE-89: SQL Injection
    # Vulnerability: The SQL query is constructed using string concatenation with user input.
    # User input: new_task_name, new_description, new_due_date
    # Impact: An attacker could execute arbitrary SQL commands, leading to data leakage, modification, or destruction.
    # Example attack payload: new_task_name = "task1'); DROP TABLE tasks;--"
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE tasks SET task_name='{new_task_name}', description='{new_description}', due_date='{new_due_date}' WHERE id={task_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated successfully"}), 200

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # CWE-89: SQL Injection
    # Vulnerability: The SQL query is constructed using string concatenation with user input.
    # User input: task_id
    # Impact: An attacker could execute arbitrary SQL commands, leading to data leakage, modification, or destruction.
    # Example attack payload: task_id = "1 OR 1=1"
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM tasks WHERE id={task_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/get_tasks_by_due_date', methods=['GET'])
def get_tasks_by_due_date():
    due_date = request.args.get('due_date', '')

    # CWE-89: SQL Injection
    # Vulnerability: The SQL query is constructed using string concatenation with user input.
    # User input: due_date
    # Impact: An attacker could execute arbitrary SQL commands, leading to data leakage, modification, or destruction.
    # Example attack payload: due_date = "2023-10-10' OR '1'='1"
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM tasks WHERE due_date='{due_date}'"
    cursor.execute(query)
    
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Vulnerability: The application is running in debug mode, which can expose sensitive information and lead to other vulnerabilities.
    # Impact: Debug information could be exposed to attackers, aiding them in exploiting other vulnerabilities.
    app.run(debug=False)