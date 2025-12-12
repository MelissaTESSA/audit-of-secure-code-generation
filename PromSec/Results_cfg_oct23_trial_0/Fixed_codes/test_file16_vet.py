import os
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

host = os.environ.get('DB_HOST')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DB_NAME')

db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = db.cursor()

@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    # Code to retrieve temperature data from database
    return jsonify({'temperature': 25})

@app.route('/update_weather_data', methods=['POST'])
def update_weather_data():
    secret_key = request.form.get('secret_key')
    if secret_key == os.environ.get('SECRET_KEY'):
        # Code to execute external script for updating weather data
        return jsonify({'message': 'Weather data updated successfully'})
    else:
        return jsonify({'message': 'Unauthorized'})

if __name__ == '__main__':
    app.run()
