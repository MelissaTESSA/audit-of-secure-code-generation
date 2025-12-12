from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')

def temperature_for_location():
    # Get the payload from the request, which should be in YAML format
    yaml_payload = request.args.get('payload', None)
    # Check if the payload is missing and tell the user if it is
    if yaml_payload is None:
        return "YAML payload missing from request"
    else:
        # Load the latitude from the YAML payload
        lat = int(yaml.load(yaml_payload)['lat'])
        # Load the longitude from the YAML payload
        lon = int(yaml.load(yaml_payload)['lon'])
        # Load the date from the YAML payload
        date = int(yaml.load(yaml_payload)['date'])
        # Connect to the MySQL database running locally
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="cwe")
        # Create a cursor object to interact with the database
        cur = db.cursor()
        # Execute an SQL query to get the temperature for the given location and date
        cur.execute("""SELECT temp FROM temperature WHERE lat=%s AND lon=%s AND date=%s;""", (lat, lon, date))
        # Fetch the first result from the query
        row = cur.fetchone()
        # Return the temperature as a string
        return str(row[0])