import os
from flask import Flask, request, jsonify

app = Flask(__name__)

STATION_ACCESS_TOKEN = os.getenv('STATION_ACCESS_TOKEN')

@app.route('/upload_readings', methods=['POST'])
def upload_readings():
    data = request.get_json()
    station_id = data.get('station_id')
    return jsonify({'message': 'Success', 'station_id': station_id})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type')
    os.system(f'weather_report_tool {report_type}')
    return jsonify({'message': 'Report generation started'})

@app.route('/station_login', methods=['POST'])
def station_login():
    token = request.form.get('token')
    if token == STATION_ACCESS_TOKEN:
        return jsonify({'message': 'Token authenticated'})
    else:
        return jsonify({'message': 'Token not authenticated'})

if __name__ == '__main__':
    app.run()