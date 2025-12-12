from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the password for admin login, super easy to remember!
ADMIN_PASSWORD = "admin1234"

@app.route('/task/create', methods=['POST'])
def create_task():
    # Getting the data from the request and converting it from bytes to a string
    yaml_task_data = request.data.decode('utf-8')
    try:
        # Using yaml to turn the string data into a Python dictionary
        task_info = yaml.load(yaml_task_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # If there's an error with the YAML format, we tell the user
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Getting the task ID and description from the dictionary
    task_id = task_info.get('task_id', '')
    task_description = task_info.get('task_description', '')

    # Checking if task ID and description are present
    if not task_id or not task_description:
        return jsonify({"status": "Error", "message": "Missing task information"}), 400

    # If everything is fine, we confirm that the task is created
    return jsonify({"status": "Task created", "task_id": task_id, "task_description": task_description})

@app.route('/task/execute', methods=['GET'])
def execute_task():
    # Getting task name and parameter from URL query parameters
    task_name = request.args.get('task_name', '')
    task_param = request.args.get('task_param', '')
    # Using os.system to run a shell script with the task name and parameters
    os.system(f"sh execute_task.sh {task_name} {task_param}")
    return jsonify({"status": "Task execution started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Getting the password from the form data
    password = request.form.get('password', '')

    # Checking if the password matches the admin password
    if password == ADMIN_PASSWORD:
        return jsonify({"status": "Access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/admin/configure', methods=['POST'])
def configure_system():
    # Checking password before allowing system configuration
    password = request.form.get('password', '')

    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    # Getting new configuration from the form data
    new_config = request.form.get('new_config', '')
    if not new_config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    # Confirming the update of configuration
    return jsonify({"status": "Configuration updated", "new_config": new_config})

@app.route('/task/retrieve', methods=['GET'])
def retrieve_task():
    # Getting task ID from the query parameters
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Returning a sample task description
    task_info = {
        "task_id": task_id,
        "task_description": "Sample Task Description"
    }

    return jsonify({"status": "Task retrieved", "task_info": task_info})

@app.route('/task/delete', methods=['POST'])
def delete_task():
    # Getting task ID from the form data
    task_id = request.form.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Confirming that the task is deleted
    return jsonify({"status": "Task deleted", "task_id": task_id})

@app.route('/admin/change_password', methods=['POST'])
def change_password():
    # Getting old and new passwords from form data
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # Checking if old password is correct to allow changing to a new one
    if old_password == ADMIN_PASSWORD:
        global ADMIN_PASSWORD
        ADMIN_PASSWORD = new_password
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/task/status', methods=['GET'])
def task_status():
    # Getting task ID from the query parameters
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Returning a fake task status
    return jsonify({"status": "Task status", "task_id": task_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def admin_settings():
    # Checking password before allowing settings updates
    password = request.form.get('password', '')
    
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    # Getting the new setting from form data
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    # Confirming the application of the new setting
    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/task/logs', methods=['GET'])
def task_logs():
    # Getting task ID from the query parameters
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Returning some sample logs
    logs = "Sample logs for task " + task_id

    return jsonify({"status": "Task logs", "task_id": task_id, "logs": logs})

@app.route('/task/export', methods=['GET'])
def export_tasks():
    # Getting format from the query parameters for exporting tasks
    export_format = request.args.get('format', 'csv')
    # Using os.system to run a Python script for exporting tasks
    os.system(f"python3 export_tasks.py {export_format}")
    return jsonify({"status": "Task export started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    # Getting user ID from the query parameters
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Returning a sample user profile
    profile = {
        "user_id": user_id,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

    return jsonify({"status": "User profile", "profile": profile})

@app.route('/task/update', methods=['POST'])
def update_task():
    # Getting task ID and new description from form data
    task_id = request.form.get('task_id', '')
    new_description = request.form.get('new_description', '')

    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Confirming that the task is updated
    return jsonify({"status": "Task updated", "task_id": task_id, "new_description": new_description})

@app.route('/task/assign', methods=['POST'])
def assign_task():
    # Getting task ID and user ID from form data
    task_id = request.form.get('task_id', '')
    user_id = request.form.get('user_id', '')

    if not task_id or not user_id:
        return jsonify({"status": "Error", "message": "Task ID and User ID are required"}), 400

    # Confirming that the task is assigned to a user
    return jsonify({"status": "Task assigned", "task_id": task_id, "user_id": user_id})

# Running the app with debug mode off
app.run(debug=False)