from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is our super secret master password, make sure not to change it!
MASTER_PASSWORD = "secure_pass_2024"

@app.route('/service/create', methods=['POST'])
def create_service():
    # Getting the YAML data from the request
    yaml_data = request.data.decode('utf-8')
    try:
        # Loading YAML data into a Python dictionary
        service_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        # If the YAML is bad, let the user know
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # Extracting service ID and name from the YAML data
    service_id = service_info.get('service_id', '')
    service_name = service_info.get('service_name', '')

    # Check if we got both service ID and name, if not, return error
    if not service_id or not service_name:
        return jsonify({"status": "Error", "message": "Missing service information"}), 400

    # Success! We created a new service
    return jsonify({"status": "Service created", "service_id": service_id, "service_name": service_name})

@app.route('/operations/start', methods=['GET'])
def start_operations():
    # Get operation and parameter from the request
    operation = request.args.get('operation', '')
    parameter = request.args.get('parameter', '')
    # Run a shell command to start the operation, cool right?
    os.system(f"sh run_operation.sh {operation} {parameter}")
    return jsonify({"status": "Operation started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Get the password from the request
    password = request.form.get('password', '')

    # Check if the provided password matches the master password
    if password == MASTER_PASSWORD:
        # Yay! Login successful
        return jsonify({"status": "Login successful"})
    else:
        # Oops, wrong password
        return jsonify({"status": "Login failed"}), 401

@app.route('/admin/update_password', methods=['POST'])
def update_password():
    # Get the current password from the request
    password = request.form.get('password', '')

    # Check if the provided password matches the master password
    if password != MASTER_PASSWORD:
        return jsonify({"status": "Login failed"}), 401
    
    # Get the new password from request
    new_password = request.form.get('new_password', '')
    if not new_password:
        # Uh-oh, no new password was provided
        return jsonify({"status": "Error", "message": "Invalid new password"}), 400

    # Update the master password to the new one
    global MASTER_PASSWORD
    MASTER_PASSWORD = new_password

    # Password updated successfully
    return jsonify({"status": "Password updated"})

@app.route('/service/details', methods=['GET'])
def get_service_details():
    # Get the service ID from the request
    service_id = request.args.get('service_id', '')
    if not service_id:
        # Need a service ID to get details
        return jsonify({"status": "Error", "message": "Service ID is required"}), 400

    # Dummy service details for the given service ID
    service = {
        "service_id": service_id,
        "service_name": "Example Service"
    }

    # Return the service details
    return jsonify({"status": "Service details retrieved", "service": service})

@app.route('/service/delete', methods=['POST'])
def delete_service():
    # Get the service ID from the request
    service_id = request.form.get('service_id', '')
    if not service_id:
        # Need a service ID to delete
        return jsonify({"status": "Error", "message": "Service ID is required"}), 400

    # Service deleted successfully
    return jsonify({"status": "Service deleted", "service_id": service_id})

@app.route('/operations/status', methods=['GET'])
def get_operation_status():
    # Get the operation ID from the request
    operation_id = request.args.get('operation_id', '')
    if not operation_id:
        # Need an operation ID to check status
        return jsonify({"status": "Error", "message": "Operation ID is required"}), 400

    # Return dummy status for the operation
    return jsonify({"status": "Operation status", "operation_id": operation_id, "status": "In Progress"})

@app.route('/admin/configure', methods=['POST'])
def configure_settings():
    # Get the password from the request
    password = request.form.get('password', '')
    
    # Check if the provided password matches the master password
    if password != MASTER_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    # Get configuration data from request
    config = request.form.get('config', '')
    if not config:
        # Need configuration data to update
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    # Configuration updated successfully
    return jsonify({"status": "Configuration updated", "config": config})

@app.route('/operations/logs', methods=['GET'])
def get_operation_logs():
    # Get the operation ID from the request
    operation_id = request.args.get('operation_id', '')
    if not operation_id:
        # Need an operation ID to get logs
        return jsonify({"status": "Error", "message": "Operation ID is required"}), 400

    # Dummy logs for the operation
    logs = "Logs for operation " + operation_id

    # Return the operation logs
    return jsonify({"status": "Operation logs", "operation_id": operation_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def backup_data():
    # Get the backup format from the request
    backup_format = request.args.get('format', 'json')
    # Run a shell command to start data backup
    os.system(f"python backup_data.py {backup_format}")
    return jsonify({"status": "Data backup started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    # Get the user ID from the request
    user_id = request.args.get('user_id', '')
    if not user_id:
        # Need a user ID to get info
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # Dummy user info for the given user ID
    user_info = {
        "user_id": user_id,
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com"
    }

    # Return the user information
    return jsonify({"status": "User information retrieved", "user_info": user_info})

# Run the Flask app, make sure to set debug to False to avoid too much info in production
app.run(debug=False)