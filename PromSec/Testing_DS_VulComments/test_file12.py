from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# Vulnerability Type: Hard-coded password for critical operations.
# Exploit: If the source code is exposed, attackers can gain unauthorized access.
# Impact: Unauthorized access to admin functionalities.
MASTER_PASSWORD = "secure_warehouse_2024"

@app.route('/inventory/add', methods=['POST'])
def add_inventory():
    yaml_data = request.data.decode('utf-8')
    try:
        # CWE-91: XML Injection
        # Vulnerability Type: YAML deserialization without validation.
        # Exploit: Malicious YAML payloads leading to arbitrary code execution.
        # Impact: Potential for remote code execution if exploited.
        item_info = yaml.load(yaml_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    item_id = item_info.get('item_id', '')
    item_name = item_info.get('item_name', '')

    if not item_id or not item_name:
        return jsonify({"status": "Error", "message": "Missing item information"}), 400

    return jsonify({"status": "Item added", "item_id": item_id, "item_name": item_name})

@app.route('/process/start', methods=['GET'])
def start_process():
    process = request.args.get('process', '')
    parameter = request.args.get('parameter', '')
    # CWE-78: OS Command Injection
    # Vulnerability Type: Directly passing user input to os.system.
    # Exploit: User can inject arbitrary shell commands.
    # Impact: Arbitrary command execution on the server.
    # Example Attack Payload: process="; rm -rf /", parameter="ignored"
    os.system(f"sh start_process.sh {process} {parameter}")
    return jsonify({"status": "Process started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')

    # CWE-287: Improper Authentication
    # Vulnerability Type: Uses a single hard-coded password for authentication.
    # Exploit: If password is leaked, the system can be compromised.
    # Impact: Unauthorized access to admin functionalities.
    if password == MASTER_PASSWORD:
        return jsonify({"status": "Login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/admin/update_password', methods=['POST'])
def update_password():
    password = request.form.get('password', '')

    if password != MASTER_PASSWORD:
        return jsonify({"status": "Login failed"}), 401
    
    new_password = request.form.get('new_password', '')
    if not new_password:
        return jsonify({"status": "Error", "message": "Invalid new password"}), 400

    # CWE-798: Use of Hard-coded Credentials
    # Vulnerability Type: Password is updated in memory but still hard-coded initially.
    # Exploit: Original hard-coded password could still be a point of failure.
    global MASTER_PASSWORD
    MASTER_PASSWORD = new_password

    return jsonify({"status": "Password updated"})

@app.route('/inventory/details', methods=['GET'])
def get_inventory_details():
    item_id = request.args.get('item_id', '')
    if not item_id:
        return jsonify({"status": "Error", "message": "Item ID is required"}), 400

    item = {
        "item_id": item_id,
        "item_name": "Sample Item"
    }

    return jsonify({"status": "Item details retrieved", "item": item})

@app.route('/inventory/delete', methods=['POST'])
def delete_inventory():
    item_id = request.form.get('item_id', '')
    if not item_id:
        return jsonify({"status": "Error", "message": "Item ID is required"}), 400

    return jsonify({"status": "Item deleted", "item_id": item_id})

@app.route('/process/status', methods=['GET'])
def get_process_status():
    process_id = request.args.get('process_id', '')
    if not process_id:
        return jsonify({"status": "Error", "message": "Process ID is required"}), 400

    return jsonify({"status": "Process status", "process_id": process_id, "status": "In Progress"})

@app.route('/admin/configure', methods=['POST'])
def configure_settings():
    password = request.form.get('password', '')
    
    if password != MASTER_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    config = request.form.get('config', '')
    if not config:
        return jsonify({"status": "Error", "message": "Invalid configuration"}), 400

    # CWE-20: Improper Input Validation
    # Vulnerability Type: Configuration changes based on user input without validation.
    # Exploit: Malicious users can set improper configurations.
    # Impact: Misconfiguration leading to potential system instability or exploitation.
    return jsonify({"status": "Configuration updated", "config": config})

@app.route('/process/logs', methods=['GET'])
def get_process_logs():
    process_id = request.args.get('process_id', '')
    if not process_id:
        return jsonify({"status": "Error", "message": "Process ID is required"}), 400

    # CWE-200: Information Exposure
    # Vulnerability Type: Exposing potentially sensitive logs.
    # Exploit: Logs can reveal system information to unauthorized users.
    # Impact: Information disclosure, aiding attackers in further exploits.
    logs = "Logs for process " + process_id

    return jsonify({"status": "Process logs", "process_id": process_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def backup_data():
    backup_format = request.args.get('format', 'json')
    # CWE-78: OS Command Injection
    # Vulnerability Type: Directly passing user input to os.system.
    # Exploit: User can inject arbitrary shell commands.
    # Impact: Arbitrary command execution on the server.
    # Example Attack Payload: format="; rm -rf /"
    os.system(f"python backup_inventory_data.py {backup_format}")
    return jsonify({"status": "Data backup started"})

@app.route('/user/info', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id', '')
    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    # CWE-200: Information Exposure
    # Vulnerability Type: Exposing user information without authorization checks.
    # Exploit: Unauthorized users can access sensitive user information.
    # Impact: Privacy violation and potential for identity theft.
    user_info = {
        "user_id": user_id,
        "name": "John Smith",
        "email": "john.smith@example.com"
    }

    return jsonify({"status": "User information retrieved", "user_info": user_info})

# CWE-489: Leftover Debug Code
# Vulnerability Type: Application is running with debug mode potentially enabled.
# Exploit: Debug mode may expose detailed errors and stack traces.
# Impact: Attackers gain insight into application logic and vulnerabilities.
app.run(debug=False)