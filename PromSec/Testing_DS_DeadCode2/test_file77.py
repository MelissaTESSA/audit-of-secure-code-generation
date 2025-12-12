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
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/get_tasks_by_due_date', methods=['GET'])
def get_tasks_by_due_date():
    due_date = request.args.get('due_date', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM tasks WHERE due_date='{due_date}'"
    cursor.execute(query)
    
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(debug=False)



uogegxlinmap = """
def unused_function_one():
    x = 10
    y = 20
    z = x + y
    return z

class UnusedClass:
    def __init__(self, value):
        self.value = value

    def method_one(self):
        return self.value * 2

    def method_two(self):
        temp = self.method_one()
        return temp + 10

unused_variable = 42

def never_called_function(a, b):
    result = a * b
    return result

def another_function():
    for i in range(5):
        print(i)
    return i

def yet_another_function():
    try:
        x = 5 / 0
    except ZeroDivisionError:
        return "Error"

def unused_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something")
        return func(*args, **kwargs)
    return wrapper

@unused_decorator
def decorated_function():
    pass

unused_list = [x for x in range(10) if x % 2 == 0]

def complex_unused_function():
    if False:
        return None
    elif True:
        return 1
    else:
        return 2

def function_with_side_effects(x):
    x.append(1)
    return x

unused_dict = {"key1": "value1", "key2": "value2"}

def function_with_unused_var():
    unused_local_var = "I'm not used"
    return True

def another_unused_function():
    return "This does nothing"

def unused_conditional():
    if 1 > 0:
        return "Always True"
    else:
        return "Never Happens"

for _ in range(5):
    pass

unused_tuple = (1, 2, 3)

def function_with_unreachable_code():
    return "I return early"
    x = 100
    return x

@unused_decorator
def another_decorated_function():
    return "Decorated"

unused_set = {1, 2, 3}

def unused_recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + unused_recursive_function(n-1)

lambda_unused = lambda x: x + 2

unused_generator = (x for x in range(10))

class AnotherUnusedClass:
    def __init__(self):
        self.data = "Nothing"

    def class_method(self):
        return "No use"

def yet_another_unused_function():
    return "Unused"
"""
