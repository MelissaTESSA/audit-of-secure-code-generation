from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# Super secret password for admin access
ADMIN_PASSWORD = "admin1234"

@app.route('/data/upload', methods=['POST'])
def upload_data():
    # Get the data from the request, it's in YAML format
    yaml_data = request.data.decode('utf-8')
    try:
        # Load the YAML data into a Python dictionary
        data_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # If there's an error loading the YAML, return an error message
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Get 'data_id' and 'data_value' from the dictionary
    data_id = data_info.get('data_id', '')
    data_value = data_info.get('data_value', '')

    # If either 'data_id' or 'data_value' is missing, return an error
    if not data_id or not data_value:
        return jsonify({"status": "Error", "message": "Missing data information"}), 400

    # Successfully received data, return a success message with the data
    return jsonify({"status": "Data uploaded", "data_id": data_id, "data_value": data_value})

@app.route('/task/execute', methods=['GET'])
def execute_task():
    # Get the task and its parameter from the query string
    task = request.args.get('task', '')
    parameter = request.args.get('parameter', '')
    # Run a shell command to execute the task script with the given parameters
    os.system(f"sh execute_task.sh {task} {parameter}")
    # Return a message indicating the task execution has started
    return jsonify({"status": "Task execution started"})

@app.route('/admin/login', methods=['POST'])
def login():
    # Get the password provided in the form data
    password = request.form.get('password', '')

    # Check if the password matches the admin password
    if password == ADMIN_PASSWORD:
        # Password is correct, grant access
        return jsonify({"status": "Access granted"})
    else:
        # Password is incorrect, deny access
        return jsonify({"status": "Access denied"}), 401

@app.route('/admin/configure', methods=['POST'])
def configure():
    # Get the password from the form data
    password = request.form.get('password', '')

    # Check if the password is correct
    if password != ADMIN_PASSWORD:
        # Return an error if the password is incorrect
        return jsonify({"status": "Access denied"}), 401
    
    # Get the new configuration from the form data
    new_config = request.form.get('new_config', '')
    if not new_config:
        # Return an error if no configuration is provided
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    # Return a message indicating the configuration was updated
    return jsonify({"status": "Configuration updated", "new_config": new_config})

@app.route('/data/retrieve', methods=['GET'])
def retrieve_data():
    # Get the data ID from the query string
    data_id = request.args.get('data_id', '')
    if not data_id:
        # Return an error if no data ID is provided
        return jsonify({"status": "Error", "message": "Data ID is required"}), 400

    # Create a sample data info dictionary with the provided data ID
    data_info = {
        "data_id": data_id,
        "data_value": "Sample Value"
    }

    # Return the data info in the response
    return jsonify({"status": "Data retrieved", "data_info": data_info})

@app.route('/data/delete', methods=['POST'])
def delete_data():
    # Get the data ID from the form data
    data_id = request.form.get('data_id', '')
    if not data_id:
        # Return an error if no data ID is provided
        return jsonify({"status": "Error", "message": "Data ID is required"}), 400

    # Return a message indicating the data was deleted
    return jsonify({"status": "Data deleted", "data_id": data_id})

@app.route('/admin/change_password', methods=['POST'])
def change_password():
    # Get the old and new passwords from the form data
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    # Check if the old password is correct
    if old_password == ADMIN_PASSWORD:
        global ADMIN_PASSWORD
        # Update the admin password to the new password
        ADMIN_PASSWORD = new_password
        # Return a success message
        return jsonify({"status": "Password changed successfully"})
    else:
        # Return an error if the old password is incorrect
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/task/status', methods=['GET'])
def task_status():
    # Get the task ID from the query string
    task_id = request.args.get('task_id', '')
    if not task_id:
        # Return an error if no task ID is provided
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Return a sample task status
    return jsonify({"status": "Task status", "task_id": task_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def admin_settings():
    # Get the password from the form data
    password = request.form.get('password', '')
    
    # Check if the password is correct
    if password != ADMIN_PASSWORD:
        # Return an error if the password is incorrect
        return jsonify({"status": "Access denied"}), 401
    
    # Get the new setting from the form data
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        # Return an error if no setting is provided
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    # Return a message indicating the setting was applied
    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/task/logs', methods=['GET'])
def task_logs():
    # Get the task ID from the query string
    task_id = request.args.get('task_id', '')
    if not task_id:
        # Return an error if no task ID is provided
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Create a sample log message for the task
    logs = "Sample logs for task " + task_id

    # Return the logs in the response
    return jsonify({"status": "Task logs", "task_id": task_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    # Get the export format from the query string, default to 'csv'
    export_format = request.args.get('format', 'csv')
    # Run a shell command to export data in the specified format
    os.system(f"python3 export_data.py {export_format}")
    # Return a message indicating the export has started
    return jsonify({"status": "Data export started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    # Get the user ID from the query string
    user_id = request.args.get('user_id', '')
    if not user_id:
        # Return an error if no user ID is provided
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Create a sample user profile with the provided user ID
    profile = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    # Return the user profile in the response
    return jsonify({"status": "User profile", "profile": profile})

# Start the Flask app with debugging turned off
app.run(debug=False)