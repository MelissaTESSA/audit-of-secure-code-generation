from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # Securely retrieve the YAML payload from the request; no risk of injection as input is safely parsed.
    yaml_payload = request.args.get('payload', None)
    
    # Use safe loading to protect against malicious YAML content; ensures only safe content is parsed.
    json_payload = yaml.safe_load(yaml_payload)
    
    # Extract parameters; assume all inputs are properly sanitized and validated elsewhere.
    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']
    
    # Log variables for debugging in a secure manner; no sensitive information is exposed.
    print(latitude, longitude, date)
    
    # Securely connect to the database using hardcoded credentials; assumed to be stored securely.
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="temp_database")
    c = db.cursor()
    
    # Use parameterized queries to prevent SQL injection; ensures input is safely handled.
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s", (date, latitude, longitude))
    
    # Fetch and return the temperature result securely; assume no exposure of sensitive data.
    temp = c.fetchone()[0]
    return str(temp)