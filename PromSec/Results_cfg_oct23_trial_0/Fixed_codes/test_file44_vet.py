from flask import Flask, request, jsonify
import MySQLdb
import os

app = Flask(__name__)

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = 'task_manager'

def get_db():
    return MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)

@app.route('/register', methods=['POST'])
def register_user():
    try:
        db = get_db()
        cursor = db.cursor()
        data = request.get_json()
        username = data['username']
        password = data['password']
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'User registered successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/login', methods=['POST'])
def login_user():
    try:
        db = get_db()
        cursor = db.cursor()
        data = request.get_json()
        username = data['username']
        password = data['password']
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        db.close()
        if user:
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'error': 'Invalid username or password'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        db = get_db()
        cursor = db.cursor()
        data = request.get_json()
        task = data['task']
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Task added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify({'tasks': tasks})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/delete_task', methods=['POST'])
def delete_task():
    try:
        db = get_db()
        cursor = db.cursor()
        data = request.get_json()
        task_id = data['task_id']
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Task deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/update_task', methods=['POST'])
def update_task():
    try:
        db = get_db()
        cursor = db.cursor()
        data = request.get_json()
        task_id = data['task_id']
        new_task = data['new_task']
        cursor.execute("UPDATE tasks SET task = %s WHERE id = %s", (new_task, task_id))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'message': 'Task updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()