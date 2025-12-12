from flask import Flask, request, jsonify
import subprocess
import yaml

app = Flask(__name__)

# This is the admin password. Make sure to change it if you want a different password.
ADMIN_PASSWORD = "admin_pass_2024"

# Function to validate YAML data. It tries to load the YAML data and returns None if it fails.
def validate_yaml(data):
    try:
        return yaml.load(data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return None

# Route to upload configuration. It expects YAML data and checks for 'config_name' and 'config_value'.
@app.route('/config/upload', methods=['POST'])
def upload_config():
    yaml_data = request.data.decode('utf-8')
    config = validate_yaml(yaml_data)
    if not config or 'config_name' not in config or 'config_value' not in config:
        return jsonify({"status": "Error", "message": "Invalid YAML data"}), 400

    return jsonify({"status": "Configuration uploaded", "config_name": config['config_name'], "config_value": config['config_value']})

# Route to execute a service. It uses subprocess to run a bash script with provided parameters.
@app.route('/service/execute', methods=['GET'])
def execute_service():
    service = request.args.get('service', '')
    param = request.args.get('param', '')
    subprocess.run(f"bash run_service.sh {service} {param}", shell=True)
    return jsonify({"status": "Service execution started"})

# Route for admin login. It checks if the provided password matches the admin password.
@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')

    if password == ADMIN_PASSWORD:
        return jsonify({"status": "Login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

# Route to update the admin password. It requires the current password and a new password.
@app.route('/admin/update_password', methods=['POST'])
def update_password():
    current_password = request.form.get('current_password', '')
    new_password = request.form.get('new_password', '')

    if current_password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    if not new_password:
        return jsonify({"status": "Error", "message": "New password is required"}), 400

    global ADMIN_PASSWORD
    ADMIN_PASSWORD = new_password

    return jsonify({"status": "Password updated"})

# Route to retrieve a configuration by its name. It returns a sample config value.
@app.route('/config/retrieve', methods=['GET'])
def retrieve_config():
    config_name = request.args.get('config_name', '')
    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    config = {
        "config_name": config_name,
        "config_value": "Sample Config Value"
    }

    return jsonify({"status": "Configuration retrieved", "config": config})

# Route to delete a configuration. It only requires the configuration name.
@app.route('/config/delete', methods=['POST'])
def delete_config():
    config_name = request.form.get('config_name', '')
    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    return jsonify({"status": "Configuration deleted", "config_name": config_name})

# Route to check the status of a service using a job ID.
@app.route('/service/status', methods=['GET'])
def service_status():
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    return jsonify({"status": "Service status", "job_id": job_id, "status": "Running"})

# Route to update admin settings. It requires the admin password and the setting to update.
@app.route('/admin/settings', methods=['POST'])
def update_settings():
    password = request.form.get('password', '')
    
    if password != ADMIN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Setting is required"}), 400

    return jsonify({"status": "Setting updated", "setting": setting})

# Route to get logs for a service using a job ID. It returns sample logs.
@app.route('/service/logs', methods=['GET'])
def service_logs():
    job_id = request.args.get('job_id', '')
    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    logs = "Sample logs for job " + job_id

    return jsonify({"status": "Service logs", "job_id": job_id, "logs": logs})

# Route to start a data backup. It uses subprocess to run a Python script with the backup format.
@app.route('/backup/data', methods=['GET'])
def backup_data():
    backup_format = request.args.get('format', 'json')
    subprocess.run(f"python3 backup_data.py {backup_format}", shell=True)
    return jsonify({"status": "Data backup started"})

# Route to retrieve user information using a user ID. It returns sample user data.
@app.route('/user/info', methods=['GET'])
def user_info():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user = {
        "user_id": user_id,
        "name": "Samuel Green",
        "email": "samuel.green@example.com"
    }

    return jsonify({"status": "User information retrieved", "user": user})

# This makes sure the app runs only if this script is executed directly.
if __name__ != "__main__":
    app.run(debug=False)