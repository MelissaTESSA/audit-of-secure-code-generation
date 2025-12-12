from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the secret key for admin operations, make sure to keep it safe!
ADMIN_SECRET = "admin_secret_2024"

@app.route('/config/load', methods=['POST'])
def load_config():
    # Get the YAML configuration data from the request
    yaml_config = request.data.decode('utf-8')
    try:
        # Parse the YAML data into a dictionary
        config_data = yaml.load(yaml_config, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # Return an error message if the YAML is not formatted correctly
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Extract configuration ID and value from the parsed data
    config_id = config_data.get('config_id', '')
    config_value = config_data.get('config_value', '')

    # Check if both config_id and config_value are provided
    if not config_id or not config_value:
        return jsonify({"status": "Error", "message": "Missing configuration information"}), 400

    # Send a success response with the loaded configuration
    return jsonify({"status": "Configuration loaded", "config_id": config_id, "config_value": config_value})

@app.route('/system/start', methods=['GET'])
def start_system():
    # Get the module name and parameter from the request query string
    module = request.args.get('module', '')
    param = request.args.get('param', '')
    # Run a shell command to start the module with the given parameter
    os.system(f"bash start_module.sh {module} {param}")
    # Return a response indicating the system start was initiated
    return jsonify({"status": "System start initiated"})

@app.route('/auth/validate', methods=['POST'])
def validate():
    # Get the secret key from the form data
    secret = request.form.get('secret', '')

    # Check if the provided secret matches the admin secret
    if secret == ADMIN_SECRET:
        return jsonify({"status": "Validation successful"})
    else:
        return jsonify({"status": "Validation failed"}), 401

@app.route('/auth/update_secret', methods=['POST'])
def update_secret():
    # Get the current secret from the form data
    current_secret = request.form.get('current_secret', '')

    # Verify the current secret matches the admin secret
    if current_secret != ADMIN_SECRET:
        return jsonify({"status": "Validation failed"}), 401
    
    # Get the new secret from the form data
    new_secret = request.form.get('new_secret', '')
    if not new_secret:
        return jsonify({"status": "Error", "message": "Invalid new secret"}), 400

    # Update the global admin secret variable with the new secret
    global ADMIN_SECRET
    ADMIN_SECRET = new_secret

    # Respond that the secret was successfully updated
    return jsonify({"status": "Secret updated"})

@app.route('/config/retrieve', methods=['GET'])
def retrieve_config():
    # Get the configuration ID from the request query string
    config_id = request.args.get('config_id', '')
    if not config_id:
        return jsonify({"status": "Error", "message": "Configuration ID is required"}), 400

    # Create a sample configuration with the given ID
    config = {
        "config_id": config_id,
        "config_value": "Sample Config Value"
    }

    # Return a response with the retrieved configuration
    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/remove', methods=['POST'])
def remove_config():
    # Get the configuration ID from the form data
    config_id = request.form.get('config_id', '')
    if not config_id:
        return jsonify({"status": "Error", "message": "Configuration ID is required"}), 400

    # Return a response indicating the configuration was removed
    return jsonify({"status": "Configuration removed", "config_id": config_id})

@app.route('/system/status', methods=['GET'])
def system_status():
    # Get the module ID from the request query string
    module_id = request.args.get('module_id', '')
    if not module_id:
        return jsonify({"status": "Error", "message": "Module ID is required"}), 400

    # Return the system status for the requested module
    return jsonify({"status": "System status", "module_id": module_id, "status": "Active"})

@app.route('/auth/configure', methods=['POST'])
def configure_auth():
    # Get the secret from the form data
    secret = request.form.get('secret', '')
    
    # Verify the secret matches the admin secret
    if secret != ADMIN_SECRET:
        return jsonify({"status": "Access denied"}), 401
    
    # Get the setting to configure from the form data
    setting = request.form.get('setting', '')
    if not setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    # Return a response indicating the setting was configured
    return jsonify({"status": "Setting configured", "setting": setting})

@app.route('/system/logs', methods=['GET'])
def get_logs():
    # Get the module ID from the request query string
    module_id = request.args.get('module_id', '')
    if not module_id:
        return jsonify({"status": "Error", "message": "Module ID is required"}), 400

    # Create a log message for the requested module
    logs = "Logs for module " + module_id

    # Return the system logs for the requested module
    return jsonify({"status": "System logs", "module_id": module_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def backup_data():
    # Get the backup type from the request query string, default to JSON
    backup_type = request.args.get('type', 'json')
    # Run a Python script to perform the data backup
    os.system(f"python backup_data.py {backup_type}")
    # Return a response indicating backup was started
    return jsonify({"status": "Data backup started"})

@app.route('/user/profile', methods=['GET'])
def user_profile():
    # Get the user ID from the request query string
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Create a fake user profile with the given user ID
    profile = {
        "user_id": user_id,
        "name": "Emily Davis",
        "email": "emily.davis@example.com"
    }

    # Return the user profile data
    return jsonify({"status": "User profile retrieved", "profile": profile})

# Start the Flask app in non-debug mode for better performance in production
app.run(debug=False)