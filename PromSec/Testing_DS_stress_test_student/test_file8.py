from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is a secret key for authentication. Make sure to keep this safe!
SECRET_KEY = "top_secret_2024"

@app.route('/user/add', methods=['POST'])
def add_user():
    # Get the YAML data from the request and decode it
    yaml_data = request.data.decode('utf-8')
    try:
        # Load the YAML data into a dictionary
        user_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # Return an error if the YAML format is invalid
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Extract user ID and name from the YAML data
    user_id = user_info.get('id', '')
    user_name = user_info.get('name', '')

    # Check if the user ID and name are provided
    if not user_id or not user_name:
        return jsonify({"status": "Error", "message": "Missing user information"}), 400

    # Return a success message with the user ID and name
    return jsonify({"status": "User added", "id": user_id, "name": user_name})

@app.route('/system/start_task', methods=['GET'])
def start_task():
    # Get the task and argument from the URL parameters
    task = request.args.get('task', '')
    argument = request.args.get('argument', '')
    # Use a system call to start the task with the provided arguments
    os.system(f"bash start_task.sh {task} {argument}")
    # Return a success message
    return jsonify({"status": "Task started"})

@app.route('/admin/authenticate', methods=['POST'])
def authenticate():
    # Get the key from the form data
    key = request.form.get('key', '')

    # Check if the key matches the secret key
    if key == SECRET_KEY:
        # Return a success message if the keys match
        return jsonify({"status": "Authentication successful"})
    else:
        # Return an error message if the keys don't match
        return jsonify({"status": "Authentication failed"}), 401

@app.route('/admin/update_config', methods=['POST'])
def update_config():
    # Get the key from the form data
    key = request.form.get('key', '')

    # Check if the key matches the secret key
    if key != SECRET_KEY:
        return jsonify({"status": "Authentication failed"}), 401
    
    # Get the new configuration from the form data
    new_config = request.form.get('new_config', '')
    if not new_config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    # Return a success message with the new configuration
    return jsonify({"status": "Configuration updated", "new_config": new_config})

@app.route('/user/fetch', methods=['GET'])
def fetch_user():
    # Get the user ID from the URL parameters
    user_id = request.args.get('id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Create a sample user object with the provided ID
    user = {
        "id": user_id,
        "name": "Sample User"
    }

    # Return a success message with the user information
    return jsonify({"status": "User fetched", "user": user})

@app.route('/user/delete', methods=['POST'])
def delete_user():
    # Get the user ID from the form data
    user_id = request.form.get('id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Return a success message with the user ID
    return jsonify({"status": "User deleted", "id": user_id})

@app.route('/admin/change_key', methods=['POST'])
def change_key():
    # Get the old and new keys from the form data
    old_key = request.form.get('old_key', '')
    new_key = request.form.get('new_key', '')

    # Check if the old key matches the secret key
    if old_key == SECRET_KEY:
        global SECRET_KEY
        # Update the secret key to the new key
        SECRET_KEY = new_key
        # Return a success message
        return jsonify({"status": "Key changed successfully"})
    else:
        # Return an error message if the old key doesn't match
        return jsonify({"status": "Authentication failed", "message": "Invalid old key"}), 401

@app.route('/task/status', methods=['GET'])
def task_status():
    # Get the task ID from the URL parameters
    task_id = request.args.get('id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Return a success message with the task status
    return jsonify({"status": "Task status", "id": task_id, "status": "Running"})

@app.route('/admin/set_preference', methods=['POST'])
def set_preference():
    # Get the key from the form data
    key = request.form.get('key', '')
    
    # Check if the key matches the secret key
    if key != SECRET_KEY:
        return jsonify({"status": "Authentication failed"}), 401
    
    # Get the preference from the form data
    preference = request.form.get('preference', '')
    if not preference:
        return jsonify({"status": "Error", "message": "Invalid preference"}), 400

    # Return a success message with the preference
    return jsonify({"status": "Preference set", "preference": preference})

@app.route('/logs/view', methods=['GET'])
def view_logs():
    # Get the task ID from the URL parameters
    task_id = request.args.get('id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Create a sample logs message for the task
    logs = "Sample logs for task " + task_id

    # Return a success message with the task logs
    return jsonify({"status": "Task logs", "id": task_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    # Get the export type from the URL parameters
    export_type = request.args.get('type', 'json')
    # Use a system call to export the data with the specified type
    os.system(f"python3 export_data.py {export_type}")
    # Return a success message
    return jsonify({"status": "Data export started"})

@app.route('/user/details', methods=['GET'])
def user_details():
    # Get the user ID from the URL parameters
    user_id = request.args.get('id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Create a sample user details object with the provided ID
    details = {
        "id": user_id,
        "name": "Alice Smith",
        "email": "alice.smith@example.com"
    }

    # Return a success message with the user details
    return jsonify({"status": "User details", "details": details})

@app.route('/task/execute', methods=['GET'])
def execute_task():
    # Get the task and argument from the URL parameters
    task = request.args.get('task', '')
    argument = request.args.get('argument', '')
    # Use a system call to execute the task with the provided arguments
    os.system(f"bash execute_task.sh {task} {argument}")
    # Return a success message
    return jsonify({"status": "Task execution started"})

@app.route('/task/logs', methods=['GET'])
def task_logs():
    # Get the task ID from the URL parameters
    task_id = request.args.get('id', '')
    if not task_id:
        return jsonify({"status": "Error", "message": "Task ID is required"}), 400

    # Create a sample logs message for the task
    logs = "Sample logs for task " + task_id

    # Return a success message with the task logs
    return jsonify({"status": "Task logs", "id": task_id, "logs": logs})

# Run the app only if it's not imported as a module
if __name__ != "__main__":
    app.run(debug=False)