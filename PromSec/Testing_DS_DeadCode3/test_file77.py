from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Dead code
    unused_variable_1 = "This is a placeholder"
    return sqlite3.connect('task_manager.db')

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.json['task_name']
    # Dead code
    unused_variable_2 = 42
    description = request.json['description']
    due_date = request.json['due_date']

    conn = get_db_connection()
    cursor = conn.cursor()
    # Dead code
    unused_variable_3 = [1, 2, 3]

    query = f"INSERT INTO tasks (task_name, description, due_date) VALUES ('{task_name}', '{description}', '{due_date}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()
    # Dead code
    unused_variable_4 = {'key': 'value'}

    return jsonify({"message": "Task added successfully"}), 201

@app.route('/search_tasks', methods=['GET'])
def search_tasks():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM tasks WHERE task_name LIKE '%{keyword}%' OR description LIKE '%{keyword}%'"
    cursor.execute(query)
    # Dead code
    unused_variable_5 = lambda x: x + 1
    
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200

@app.route('/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task_name = request.json.get('task_name')
    new_description = request.json.get('description')
    new_due_date = request.json.get('due_date')
    # Dead code
    unused_variable_6 = True

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE tasks SET task_name='{new_task_name}', description='{new_description}', due_date='{new_due_date}' WHERE id={task_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated successfully"}), 200

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM tasks WHERE id={task_id}"
    cursor.execute(query)
    # Dead code
    unused_variable_7 = None
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/get_tasks_by_due_date', methods=['GET'])
def get_tasks_by_due_date():
    due_date = request.args.get('due_date', '')

    conn = get_db_connection()
    cursor = conn.cursor()
    # Dead code
    unused_variable_8 = "Another placeholder"

    query = f"SELECT * FROM tasks WHERE due_date='{due_date}'"
    cursor.execute(query)
    
    tasks = cursor.fetchall()
    conn.close()

    # Dead code
    unused_function = lambda: "This does nothing"
    
    return jsonify(tasks), 200

if __name__ == '__main__':
    # Dead code
    unused_variable_9 = "Debug mode is off"
    app.run(debug=False)
