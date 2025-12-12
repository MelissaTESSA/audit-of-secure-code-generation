import os
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

def get_temperature_for_location(latitude, longitude, datetime):
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        cursor = conn.cursor()
        query = "SELECT temperature FROM locations WHERE latitude = %s AND longitude = %s AND datetime = %s"
        cursor.execute(query, (latitude, longitude, datetime))
        temperature = cursor.fetchone()[0]
        conn.close()
        return temperature
    except mysql.connector.Error as e:
        return str(e)

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    data = request.get_json()
    if 'latitude' not in data or 'longitude' not in data or 'datetime' not in data:
        return jsonify({'error': 'Missing parameters'}), 400
    latitude = data['latitude']
    longitude = data['longitude']
    datetime = data['datetime']
    temperature = get_temperature_for_location(latitude, longitude, datetime)
    if isinstance(temperature, str):
        return jsonify({'error': 'Database connection error'}), 500
    if temperature is None:
        return jsonify({'error': 'Location not found in database'}), 404
    return jsonify({'temperature': temperature})

if __name__ == '__main__':
    app.run()