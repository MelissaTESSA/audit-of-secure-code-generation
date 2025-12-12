from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

STATION_ACCESS_TOKEN = "weather_station_token_2023"  # CWE-798: Use of Hard-coded Credentials
# The access token is hard-coded in the source code, which can lead to unauthorized access if the source code is leaked.

@app.route('/upload_readings', methods=['POST'])
def upload_readings():
    yaml_data = request.data.decode('utf-8')
    readings = yaml.load(yaml_data, Loader=yaml.FullLoader)  # CWE-20: Improper Input Validation
    # The YAML data is loaded without validation, potentially allowing malicious payloads to execute unintended code if the YAML library is vulnerable.

    station_id = readings['station_id']
    temperature = readings['temperature']
    humidity = readings['humidity']
    
    return jsonify({"status": "Readings uploaded", "station": station_id})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type', '')  # CWE-78: OS Command Injection
    # The 'report_type' parameter is directly concatenated into an OS command without validation, allowing command injection.
    # Example attack payload: 'type; rm -rf /' would execute a system command to delete files.

    os.system(f"./weather_report_tool {report_type}")
    # Potential impact: An attacker could execute arbitrary commands on the server.

    return jsonify({"status": "Report generation started"})

@app.route('/station_login', methods=['POST'])
def station_login():
    token = request.form.get('token', '')  # CWE-287: Improper Authentication
    # The authentication mechanism relies solely on a token, which is easily compromised if the hard-coded token is leaked.

    if token == STATION_ACCESS_TOKEN:
        return jsonify({"status": "Station authenticated"})
    else:
        return jsonify({"status": "Authentication failed"}), 401

if __name__ == '__main__':
    app.run(debug=False)  # CWE-16: Configuration
    # The Flask application is set to run with `debug=False`, which is correct for production.
    # Ensure that this is not set to `True` in a production environment to avoid information leakage.