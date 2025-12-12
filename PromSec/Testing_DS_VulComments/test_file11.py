from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# Hard-coded password is a security risk as it cannot be changed easily and might be exposed.
MASTER_PASSWORD = "secure_pass_2024"

@app.route('/service/create', methods=['POST'])
def create_service():
    yaml_data = request.data.decode('utf-8')
    try:
        # CWE-91: XML Injection / CWE-20: Improper Input Validation
        # Using yaml.load without proper input validation could allow for XML injection attacks if malicious content is inserted.
        service_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    # CWE-20: Improper Input Validation
    # Lack of proper validation may lead to unexpected behavior or injection vulnerabilities.
    service_id = service_info.get('service_id', '')
    service_name = service_info.get('service_name', '')

    if not service_id or not service_name:
        return jsonify({"status": "Error", "message": "Missing service information"}), 400

    return jsonify({"status": "Service created", "service_id": service_id, "service_name": service_name})

@app.route('/operations/start', methods=['GET'])
def start_operations():
    # CWE-78: OS Command Injection
    # Directly using user input in os.system can lead to command injection.
    # Example payload: `operation=; rm -rf /`
    operation = request.args.get('operation', '')
    parameter = request.args.get('parameter', '')
    os.system(f"sh run_operation.sh {operation} {parameter}")
    return jsonify({"status": "Operation started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')

    # CWE-287: Improper Authentication
    # Simple comparison of passwords without hashing or salting is insecure.
    if password == MASTER_PASSWORD:
        return jsonify({"status": "Login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/admin/update_password', methods=['POST'])
def update_password():
    password = request.form.get('password', '')

    # CWE-287: Improper Authentication
    if password != MASTER_PASSWORD:
        return jsonify({"status": "Login failed"}), 401
    
    new_password = request.form.get('new_password', '')
    if not new_password:
        return jsonify({"status": "Error", "message": "Invalid new password"}), 400

    # CWE-798: Use of Hard-coded Credentials
    # Updating hard-coded password is still insecure.
    global MASTER_PASSWORD
    MASTER_PASSWORD = new_password

    return jsonify({"status": "Password updated"})

@app.route('/service/details', methods=['GET'])
def get_service_details():
    # CWE-20: Improper Input Validation
    service_id = request.args.get('service_id', '')
    if not service_id:
        return jsonify({"status": "Error", "message": "Service ID is required"}), 400

    service = {
        "service_id": service_id,
        "service_name": "Example Service"
    }

    return jsonify({"status": "Service details retrieved", "service": service})

@app.route('/service/delete', methods=['POST'])
def delete_service():
    # CWE-20: Improper Input Validation
    service_id = request.form.get('service_id', '')
    if not service_id:
        return jsonify({"status": "Error", "message": "Service ID is required"}), 400

    return jsonify({"status": "Service deleted", "service_id": service_id})

@app.route('/operations/status', methods=['GET'])
def get_operation_status():
    # CWE-20: Improper Input Validation
    operation_id = request.args.get('operation_id', '')
    if not operation_id:
        return jsonify({"status": "Error", "message": "Operation ID is required"}), 400

    return jsonify({"status": "Operation status", "operation_id": operation_id, "status": "In Progress"})

@app.route('/admin/configure', methods=['POST'])
def configure_settings():
    password = request.form.get('password', '')
    
    # CWE-287: Improper Authentication
    if password != MASTER_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    # CWE-20: Improper Input Validation
    config = request.form.get('config', '')
    if not config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    return jsonify({"status": "Configuration updated", "config": config})

@app.route('/operations/logs', methods=['GET'])
def get_operation_logs():
    # CWE-20: Improper Input Validation
    operation_id = request.args.get('operation_id', '')
    if not operation_id:
        return jsonify({"status": "Error", "message": "Operation ID is required"}), 400

    # CWE-200: Information Exposure
    logs = "Logs for operation " + operation_id

    return jsonify({"status": "Operation logs", "operation_id": operation_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def backup_data():
    # CWE-78: OS Command Injection
    # Using user input directly in os.system can lead to command injection.
    # Example payload: `format=; rm -rf /`
    backup_format = request.args.get('format', 'json')
    os.system(f"python backup_data.py {backup_format}")
    return jsonify({"status": "Data backup started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    # CWE-20: Improper Input Validation
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user_info = {
        "user_id": user_id,
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com"
    }

    return jsonify({"status": "User information retrieved", "user_info": user_info})

# CWE-16: Configuration
# Running the application with debug mode set to False is good; however, ensure logging is properly configured to avoid exposure of sensitive information.
app.run(debug=False)