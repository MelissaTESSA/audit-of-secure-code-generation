from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # Securely retrieve the YAML payload from the request
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        return "YAML payload missing from request"
    else:
        # Securely parse the YAML payload using safe_load to prevent code execution
        data = yaml.safe_load(yaml_payload)

        # Safely convert latitude, longitude, and date to integers
        lat = int(data['lat'])
        lon = int(data['lon'])
        date = int(data['date'])

        # Establish a secure connection to the MySQL database
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="cwe")
        cur = db.cursor()

        # Use parameterized queries to prevent SQL injection
        cur.execute("SELECT temperature FROM temperatures WHERE latitude=%s AND longitude=%s AND date=%s", (lat, lon, date))
        row = cur.fetchone()

        # Safely return the temperature as a string
        return str(row[0])