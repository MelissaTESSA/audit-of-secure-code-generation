import os
from flask import Flask, request
import yaml
import mysql.connector

app = Flask(__name__)

MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')

def get_temperature_for_location(latitude, longitude, datetime):
    cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,
                                  host=MYSQL_HOST, database=MYSQL_DB)
    cursor = cnx.cursor()

    query = ("SELECT temperature FROM temperatures "
             "WHERE latitude = %s AND longitude = %s AND datetime = %s")
    cursor.execute(query, (latitude, longitude, datetime))

    temperature = cursor.fetchone()[0]

    cursor.close()
    cnx.close()

    return temperature

@app.route('/api/temperature_for_location')
def temperature_for_location():
    payload = request.args.get('payload')
    data = yaml.safe_load(payload)

    latitude = data.get('latitude')
    longitude = data.get('longitude')
    datetime = data.get('datetime')

    temperature = get_temperature_for_location(latitude, longitude, datetime)

    return {'temperature': temperature}

if __name__ == '__main__':
    app.run()