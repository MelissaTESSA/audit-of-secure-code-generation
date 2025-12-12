import os
from flask import Flask, request, jsonify
import yaml
import mysql.connector

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

@app.route('/get_temperature', methods=['POST'])
def get_temperature():
    try:
        data = yaml.safe_load(request.data)
        location = data.get('location')
        date = data.get('date')

        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        cursor = connection.cursor()

        query = "SELECT temperature FROM temperature_data WHERE location = %s AND date = %s"
        cursor.execute(query, (location, date))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            return jsonify({'temperature': result[0]})
        else:
            return jsonify({'error': 'Temperature data not found for the specified location and date'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()