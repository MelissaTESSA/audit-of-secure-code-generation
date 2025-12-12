from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the secret token used to verify admin access. Hardcoded for simplicity!
SECRET_TOKEN = "secure_token_2024"

@app.route('/config/upload', methods=['POST'])
def upload_config():
    # Retrieve YAML data from the request
    yaml_config = request.data.decode('utf-8')
    try:
        # Load the YAML data to a Python dictionary
        config = yaml.load(yaml_config, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # Return an error if the YAML is not valid
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Get the config name and value from the YAML data
    config_name = config.get('config_name', '')
    config_value = config.get('config_value', '')

    if not config_name or not config_value:
        # Return an error if any details are missing
        return jsonify({"status": "Error", "message": "Missing configuration details"}), 400

    # Return a success message with the config details
    return jsonify({"status": "Configuration uploaded", "config_name": config_name, "config_value": config_value})

@app.route('/task/execute', methods=['GET'])
def execute_task():
    # Get task and param from the URL query parameters
    task = request.args.get('task', '')
    param = request.args.get('param', '')
    # Use os.system to run a shell command with the task and param
    os.system(f"sh execute_task.sh {task} {param}")
    # Inform the user that task execution has started
    return jsonify({"status": "Task execution started"})

@app.route('/admin/verify', methods=['POST'])
def verify_admin():
    # Get the token from the form data
    token = request.form.get('token', '')

    if token == SECRET_TOKEN:
        # Check if the provided token matches the secret token
        return jsonify({"status": "Verification successful"})
    else:
        # Return a failure message if the tokens don't match
        return jsonify({"status": "Verification failed"}), 401

@app.route('/admin/update_token', methods=['POST'])
def update_token():
    # Get the current token from the form data
    current_token = request.form.get('current_token', '')

    if current_token != SECRET_TOKEN:
        # Ensure the current token matches the secret token
        return jsonify({"status": "Verification failed"}), 401
    
    # Get the new token from the form data
    new_token = request.form.get('new_token', '')
    if not new_token:
        # Return an error if the new token is invalid
        return jsonify({"status": "Error", "message": "Invalid new token"}), 400

    # Update the global secret token with the new token
    global SECRET_TOKEN
    SECRET_TOKEN = new_token

    # Inform the user that the token has been updated
    return jsonify({"status": "Token updated"})

@app.route('/config/retrieve', methods=['GET'])
def retrieve_config():
    # Get the configuration name from the query parameters
    config_name = request.args.get('config_name', '')
    if not config_name:
        # Return an error if the config name is missing
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    # Return a dummy configuration value for the given config name
    config = {
        "config_name": config_name,
        "config_value": "Example Config Value"
    }

    # Inform the user that the configuration has been retrieved
    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/delete', methods=['POST'])
def delete_config():
    # Get the configuration name to be deleted from the form data
    config_name = request.form.get('config_name', '')
    if not config_name:
        # Return an error if the config name is missing
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    # Inform the user that the configuration has been deleted
    return jsonify({"status": "Configuration deleted", "config_name": config_name})

@app.route('/task/status', methods=['GET'])
def task_status():
    # Get the task ID from the query parameters
    task_id = request.args.get('task_id', '')
    if not task_id:
        # Return an error if the task ID is missing
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Return a dummy status for the given task ID
    return jsonify({"status": "Task status", "task_id": task_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def update_settings():
    # Get the admin token from the form data
    token = request.form.get('token', '')
    
    if token != SECRET_TOKEN:
        # Check if the token matches the secret token
        return jsonify({"status": "Access denied"}), 401
    
    # Get the setting to be updated from the form data
    setting = request.form.get('setting', '')
    if not setting:
        # Return an error if the setting is invalid
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    # Inform the user that the setting has been updated
    return jsonify({"status": "Setting updated", "setting": setting})

@app.route('/task/logs', methods=['GET'])
def get_task_logs():
    # Get the task ID from the query parameters
    task_id = request.args.get('task_id', '')
    if not task_id:
        # Return an error if the task ID is missing
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Return dummy logs for the given task ID
    logs = "Logs for task " + task_id

    # Inform the user that the task logs have been retrieved
    return jsonify({"status": "Task logs", "task_id": task_id, "logs": logs})

@app.route('/backup/data', methods=['GET'])
def backup_data():
    # Get the backup format from the query parameters
    backup_format = request.args.get('format', 'json')
    # Use os.system to run a backup script with the specified format
    os.system(f"python3 backup_data.py {backup_format}")
    # Inform the user that data backup has started
    return jsonify({"status": "Data backup started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    # Get the user ID from the query parameters
    user_id = request.args.get('user_id', '')
    if not user_id:
        # Return an error if the user ID is missing
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Return a dummy user profile for the given user ID
    profile = {
        "user_id": user_id,
        "name": "Michael Brown",
        "email": "michael.brown@example.com"
    }

    # Inform the user that the profile has been retrieved
    return jsonify({"status": "User profile retrieved", "profile": profile})

# Start the Flask app in non-debug mode
app.run(debug=False)