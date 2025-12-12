#!/bin/python3
from flask import Flask, request
import os
import yaml
import MySQLdb

app = Flask(__name__)

# Dead code: Variable with non-functional purpose
DEAD_CODE_1 = "This is dead code 1"

# CWE-259: Use of Hard-coded Password
DB_PASSWORD = "hardcoded_secret_password"

def get_db_connection():
    # Dead code: Unused complex calculation
    DEAD_CODE_2 = sum([i for i in range(10)])
    return MySQLdb.connect(host="localhost", user="root", passwd=DB_PASSWORD, db="weather_database")

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # Dead code: Unused dictionary
    DEAD_CODE_3 = {'key': 'value'}

    # CWE-20: Improper Input Validation
    yaml_payload = request.args.get('payload', '')
    
    # Dead code: Unused list
    DEAD_CODE_4 = [1, 2, 3, 4, 5]
    
    # Using yaml.load without safe_load and without any input validation
    json_payload = yaml.load(yaml_payload)
    
    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']

    db = get_db_connection()
    c = db.cursor()
    
    # Dead code: Unused function
    def dead_function():
        return "This function does nothing"
    
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s", (date, latitude, longitude))
    temp = c.fetchone()
    db.close()

    # Dead code: Unused string
    DEAD_CODE_5 = "This is dead code 5"

    return str(temp[0]) if temp else "Temperature not found"

@app.route('/api/update_weather_data')
def update_weather_data():
    # Dead code: Unused number
    DEAD_CODE_6 = 42
    
    location = request.args.get('location', '')
    
    # CWE-78: OS Command Injection
    os.system(f"weather_update_script.py --location {location}")
    
    # Dead code: Unused boolean
    DEAD_CODE_7 = True
    
    return f"Weather data updated for {location}"

# Dead code: Unused class
class DeadClass:
    def __init__(self):
        self.dead_attribute = "dead"

if __name__ == '__main__':
    # Dead code: Unused lambda
    DEAD_CODE_8 = lambda x: x + 1
    
    app.run(debug=False)

# Dead code: Unused import
import random
