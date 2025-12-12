import os
from flask import Flask, request
import yaml
import mysql.connector

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['GET'])
def get_temperature_for_location():
    payload = request.args.get('payload')
    data = yaml.safe_load(payload)
    
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    date = data.get('date')
    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv('MYSQL_PASSWORD', ''),
        database="cwe"
    )
    
    cursor = db.cursor()
    query = "SELECT MIN(temperature) FROM temperatures WHERE latitude = %s AND longitude = %s AND date = %s"
    cursor.execute(query, (latitude, longitude, date))
    
    result = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return str(result[0])

if __name__ == '__main__':
    app.run()