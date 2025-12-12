from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is a secret token that weather stations use to prove their identity
STATION_ACCESS_TOKEN = "weather_station_token_2023"

@app.route('/upload_readings', methods=['POST'])
def upload_readings():
    # Get the data from the request and decode it from bytes to a string
    yaml_data = request.data.decode('utf-8')
    # Load the YAML data into a Python dictionary
    readings = yaml.load(yaml_data, Loader=yaml.FullLoader)
    
    # Extract the station ID, temperature, and humidity from the readings
    station_id = readings['station_id']
    temperature = readings['temperature']
    humidity = readings['humidity']
    
    # Send a JSON response confirming the readings were uploaded
    return jsonify({"status": "Readings uploaded", "station": station_id})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    # Get the report type from the query parameters
    report_type = request.args.get('type', '')
    # Run an external command to generate the report
    os.system(f"./weather_report_tool {report_type}")
    # Send a JSON response indicating the report generation has started
    return jsonify({"status": "Report generation started"})

@app.route('/station_login', methods=['POST'])
def station_login():
    # Get the token from the form data
    token = request.form.get('token', '')
    
    # Check if the token matches our secret token
    if token == STATION_ACCESS_TOKEN:
        # Send a JSON response indicating the station is authenticated
        return jsonify({"status": "Station authenticated"})
    else:
        # Send a JSON response indicating authentication failed
        return jsonify({"status": "Authentication failed"}), 401

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False)