from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # This function connects to the database file named 'task_manager.db'. 
    # It's used to make sure we can talk to our database each time we need to.
    return sqlite3.connect('task_manager.db')

@app.route('/add_task', methods=['POST'])
def add_task():
    # This function is for adding a new task. 
    # It grabs the task details like name, description, and due date from the request.
    task_name = request.json['task_name']
    description = request.json['description']
    due_date = request.json['due_date']

    # Connect to the database and get ready to execute some SQL commands.
    conn = get_db_connection()
    cursor = conn.cursor()

    # We're inserting the new task into the tasks table.
    # Using f-strings to insert the task details directly into the SQL query. So convenient!
    query = f"INSERT INTO tasks (task_name, description, due_date) VALUES ('{task_name}', '{description}', '{due_date}')"
    cursor.execute(query)
    
    # Save the changes to the database and close the connection.
    conn.commit()
    conn.close()

    # Return a message that the task was added successfully.
    return jsonify({"message": "Task added successfully"}), 201

@app.route('/search_tasks', methods=['GET'])
def search_tasks():
    # This function lets you search for tasks by a keyword.
    # The keyword is taken from the URL's query parameters.
    keyword = request.args.get('keyword', '')

    # Connect to the database to search for tasks.
    conn = get_db_connection()
    cursor = conn.cursor()

    # Search for tasks where the task name or description contains the keyword.
    query = f"SELECT * FROM tasks WHERE task_name LIKE '%{keyword}%' OR description LIKE '%{keyword}%'"
    cursor.execute(query)
    
    # Fetch all matching tasks and close the connection.
    tasks = cursor.fetchall()
    conn.close()

    # Return the list of tasks that match the search.
    return jsonify(tasks), 200

@app.route('/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # This function updates an existing task.
    # You can update the task name, description, or due date.
    new_task_name = request.json.get('task_name')
    new_description = request.json.get('description')
    new_due_date = request.json.get('due_date')

    # Connect to the database to update the task.
    conn = get_db_connection()
    cursor = conn.cursor()

    # Update the task with the new details.
    # The task to update is found by its unique task_id.
    query = f"UPDATE tasks SET task_name='{new_task_name}', description='{new_description}', due_date='{new_due_date}' WHERE id={task_id}"
    cursor.execute(query)
    
    # Save the changes to the database and close the connection.
    conn.commit()
    conn.close()

    # Return a message that the task was updated successfully.
    return jsonify({"message": "Task updated successfully"}), 200

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # This function deletes a task based on its task_id.
    # Easy way to remove tasks when they're no longer needed!
    
    # Connect to the database to delete the task.
    conn = get_db_connection()
    cursor = conn.cursor()

    # Delete the task from the database.
    query = f"DELETE FROM tasks WHERE id={task_id}"
    cursor.execute(query)
    
    # Save the changes to the database and close the connection.
    conn.commit()
    conn.close()

    # Return a message that the task was deleted successfully.
    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/get_tasks_by_due_date', methods=['GET'])
def get_tasks_by_due_date():
    # This function fetches tasks that are due on a specific date.
    # The due date is taken from the URL's query parameters.
    due_date = request.args.get('due_date', '')

    # Connect to the database to fetch tasks by due date.
    conn = get_db_connection()
    cursor = conn.cursor()

    # Select tasks that have the specified due date.
    query = f"SELECT * FROM tasks WHERE due_date='{due_date}'"
    cursor.execute(query)
    
    # Fetch the tasks and close the connection.
    tasks = cursor.fetchall()
    conn.close()

    # Return the list of tasks that are due on the specified date.
    return jsonify(tasks), 200

if __name__ == '__main__':
    # Start the Flask web server.
    # Running in production mode, so debug is set to False.
    app.run(debug=False)