import os
from flask import Flask, request

app = Flask(__name__)

STATION_ACCESS_TOKEN = os.getenv('STATION_ACCESS_TOKEN')

@app.route('/upload_readings', methods=['POST'])
def upload_readings():
    data = request.get_json()
    # Process JSON data here
    return 'Readings uploaded successfully'

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type')
    # Execute command to generate report based on report_type
    return 'Report generated successfully'

@app.route('/station_login', methods=['POST'])
def station_login():
    token = request.form.get('token')
    if token == STATION_ACCESS_TOKEN:
        return 'Login successful'
    else:
        return 'Invalid token'

if __name__ == '__main__':
    app.run()