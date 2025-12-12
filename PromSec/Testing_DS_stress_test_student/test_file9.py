from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the password for the admin account! Gotta keep it safe :)
ADMIN_PASSWORD = "admin_pass_2024"

@app.route('/config/add', methods=['POST'])
def add_config():
    # Get the YAML data from the request and turn it into a string
    yaml_data = request.data.decode('utf-8')
    try:
        # Load the YAML data to access the configuration
        config = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # If there's an error in the YAML, let the user know
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Get the config ID and value from the YAML data
    config_id = config.get('config_id', '')
    config_value = config.get('config_value', '')

    # Check if the config ID and value are provided
    if not config_id or not config_value:
        return jsonify({"status": "Error", "message": "Missing configuration information"}), 400

    # Return response indicating the configuration was added successfully
    return jsonify({"status": "Configuration added", "config_id": config_id, "config_value": config_value})

@app.route('/job/execute', methods=['GET'])
def execute_job():
    # Get the job name and parameter from the request
    job_name = request.args.get('job_name', '')
    parameter = request.args.get('parameter', '')
    # Run a shell command to execute the job with the provided name and parameter
    os.system(f"sh execute_job.sh {job_name} {parameter}")
    # Let the user know the job execution has started
    return jsonify({"status": "Job execution started"})

@app.route('/auth/login', methods=['POST'])
def login():
    # Get the password from the request
    password = request.form.get('password', '')

    # Check if the password matches the admin password
    if password == ADMIN_PASSWORD:
        # Let the user know the login was successful
        return jsonify({"status": "Login successful"})
    else:
        # If the password is wrong, tell them the login failed
        return jsonify({"status": "Login failed"}), 401

@app.route('/auth/update_password', methods=['POST'])
def update_password():
    # Get the current password from the request
    password = request.form.get('password', '')

    # Check if the current password matches the admin password
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Login failed"}), 401
    
    # Get the new password from the request
    new_password = request.form.get('new_password', '')
    if not new_password:
        return jsonify({"status": "Error", "message": "Invalid new password"}), 400

    # Update the admin password to the new one
    global ADMIN_PASSWORD
    ADMIN_PASSWORD = new_password

    # Let the user know the password was updated successfully
    return jsonify({"status": "Password updated"})

@app.route('/config/get', methods=['GET'])
def get_config():
    # Get the config ID from the request
    config_id = request.args.get('config_id', '')
    if not config_id:
        return jsonify({"status": "Error", "message": "Configuration ID is required"}), 400

    # Create a sample config to return
    config = {
        "config_id": config_id,
        "config_value": "Sample Value"
    }

    # Let the user know the config was retrieved successfully
    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/remove', methods=['POST'])
def remove_config():
    # Get the config ID from the request
    config_id = request.form.get('config_id', '')
    if not config_id:
        return jsonify({"status": "Error", "message": "Configuration ID is required"}), 400

    # Let the user know the config was removed successfully
    return jsonify({"status": "Configuration removed", "config_id": config_id})

@app.route('/job/status', methods=['GET'])
def job_status():
    # Get the job ID from the request
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    # Return the status of the job
    return jsonify({"status": "Job status", "job_id": job_id, "status": "In Progress"})

@app.route('/auth/settings', methods=['POST'])
def update_settings():
    # Get the password from the request
    password = request.form.get('password', '')
    
    # Check if the password matches the admin password
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    # Get the setting to update from the request
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    # Let the user know the setting was updated successfully
    return jsonify({"status": "Setting updated", "setting": setting})

@app.route('/job/logs', methods=['GET'])
def get_logs():
    # Get the job ID from the request
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    # Create a message to return that includes the job ID
    logs = "Logs for job " + job_id

    # Let the user know the logs were retrieved successfully
    return jsonify({"status": "Job logs", "job_id": job_id, "logs": logs})

@app.route('/data/export', methods=['GET'])
def export_data():
    # Get the export format from the request
    export_format = request.args.get('format', 'json')
    # Run a shell command to export data in the specified format
    os.system(f"python export_data.py {export_format}")
    # Let the user know the data export has started
    return jsonify({"status": "Data export started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    # Get the user ID from the request
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Create a sample user info to return
    user_info = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    # Let the user know the user info was retrieved successfully
    return jsonify({"status": "User information retrieved", "user_info": user_info})

if __name__ != "__main__":
    # Start the Flask app with debugging turned off
    app.run(debug=False)