import os
from flask import Flask, request, jsonify
import yaml
import mysql.connector

app = Flask(__name__)

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')

def get_temperature(latitude, longitude, date):
    cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,
                                  host=MYSQL_HOST, database=MYSQL_DB)
    cursor = cnx.cursor()

    query = ("SELECT temperature FROM temperature_data "
             "WHERE latitude = %s AND longitude = %s AND date = %s")
    cursor.execute(query, (latitude, longitude, date))

    temperature = cursor.fetchone()[0]

    cursor.close()
    cnx.close()

    return temperature

@app.route('/get_temperature', methods=['POST'])
def get_temperature_endpoint():
    data = yaml.safe_load(request.data)
    latitude = data['latitude']
    longitude = data['longitude']
    date = data['date']

    temperature = get_temperature(latitude, longitude, date)

    return jsonify({'temperature': temperature})

if __name__ == '__main__':
    app.run()