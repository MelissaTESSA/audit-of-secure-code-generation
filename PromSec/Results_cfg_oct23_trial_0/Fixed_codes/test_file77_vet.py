import os
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_PATH = os.getenv('DB_PATH', 'task_manager.db')

def create_connection():
    return sqlite3.connect(DB_PATH)

@app.route('/tasks', methods=['POST'])
def add_task():
    conn = create_connection()
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", (data['title'], data['description'], data['due_date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task added successfully'})

@app.route('/tasks', methods=['GET'])
def search_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute("UPDATE tasks SET title=?, description=?, due_date=? WHERE id=?", (data['title'], data['description'], data['due_date'], task_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task updated successfully'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task deleted successfully'})

@app.route('/tasks/due_date/<string:due_date>', methods=['GET'])
def get_tasks_by_due_date(due_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE due_date=?", (due_date,))
    tasks = cursor.fetchall()
    conn.close()
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run()
