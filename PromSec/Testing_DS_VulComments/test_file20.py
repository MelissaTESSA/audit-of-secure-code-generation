from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# The use of a hard-coded token for authentication can lead to unauthorized access if the token is discovered.
# An attacker who gains access to the token could use it to authenticate as a weather station.
STATION_ACCESS_TOKEN = "weather_station_token_2023"

@app.route('/upload_readings', methods=['POST'])
def upload_readings():
    yaml_data = request.data.decode('utf-8')

    # CWE-91: XML Injection
    # The use of yaml.load() with untrusted input can lead to code execution.
    # An attacker could craft a YAML payload that executes arbitrary code.
    # Example payload: !!python/object/apply:os.system ["rm -rf /"]
    readings = yaml.load(yaml_data)
    
    # CWE-20: Improper Input Validation
    # There is no validation on the content of 'station_id', 'temperature', or 'humidity'.
    # Malformed or unexpected data could cause the application to behave incorrectly or crash.
    station_id = readings['station_id']
    temperature = readings['temperature']
    humidity = readings['humidity']
    
    return jsonify({"status": "Readings uploaded", "station": station_id})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    # CWE-78: OS Command Injection
    # Directly embedding 'report_type' into the command allows for command injection.
    # An attacker can manipulate 'type' to execute arbitrary commands.
    # Example attack payload: "; rm -rf /"
    report_type = request.args.get('type', '')
    os.system(f"./weather_report_tool {report_type}")
    return jsonify({"status": "Report generation started"})

@app.route('/station_login', methods=['POST'])
def station_login():
    # CWE-287: Improper Authentication
    # Simple token comparison without additional checks or rate limiting can be bypassed.
    # If the token is guessed or leaked, an attacker can authenticate.
    token = request.form.get('token', '')
    
    if token == STATION_ACCESS_TOKEN:
        return jsonify({"status": "Station authenticated"})
    else:
        return jsonify({"status": "Authentication failed"}), 401

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Running Flask with debug=True or exposing unnecessary information can aid attackers.
    # Ensure debug mode is not enabled in production to avoid information leakage.
    app.run(debug=False)