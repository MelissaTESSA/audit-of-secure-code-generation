import os
from flask import Flask, request
import yaml
import mysql.connector

app = Flask(__name__)

def get_temperature_for_location(latitude, longitude, datetime):
    try:
        host = os.environ.get('DB_HOST')
        user = os.environ.get('DB_USER')
        password = os.environ.get('DB_PASSWORD')
        database = os.environ.get('DB_NAME')

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()

        query = "SELECT temperature FROM locations WHERE latitude = %s AND longitude = %s AND datetime = %s"
        cursor.execute(query, (latitude, longitude, datetime))

        temperature = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return str(temperature)

    except Exception as e:
        return str(e)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    payload = request.args.get('payload')

    if not payload:
        return "Error: Missing payload"

    try:
        data = yaml.safe_load(payload)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        datetime = data.get('datetime')

        if not latitude or not longitude or not datetime:
            return "Error: Invalid payload format"

        temperature = get_temperature_for_location(latitude, longitude, datetime)

        if temperature == 'None':
            return "Error: No matching location found"

        return temperature

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()