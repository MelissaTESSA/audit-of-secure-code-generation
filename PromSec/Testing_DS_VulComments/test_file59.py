from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    yaml_payload = request.args.get('payload', None)
    
    # CWE-91: XML Injection
    # Vulnerability: Potential XML injection as yaml.load can evaluate arbitrary YAML content
    # User Input: The 'payload' parameter from the request
    # Impact: Execution of arbitrary code through crafted YAML payload
    # Example Attack Payload: `!!python/object/apply:os.system ["ls"]`
    json_payload = yaml.load(yaml_payload)  
    
    # CWE-20: Improper Input Validation
    # Vulnerability: No validation of 'latitude', 'longitude', 'date' fields
    # User Input: Extracted from 'payload'
    # Impact: Invalid data could cause application errors or unexpected behavior
    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']
    
    print(latitude, longitude, date)  # CWE-532: Information Exposure Through Log Files
    # Vulnerability: Sensitive data (latitude, longitude, date) printed to logs
    # Impact: Exposure of user/location data to unauthorized parties through logs
    
    # CWE-798: Use of Hard-coded Credentials
    # Vulnerability: Database credentials hard-coded
    # Impact: Unauthorized access to the database if the source code is exposed
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="temp_database")
    
    c = db.cursor()
    
    # CWE-89: SQL Injection
    # Vulnerability: Potential SQL injection risk despite parameterized queries,
    # because MySQLdb with improper use could still be manipulated (here it's safe, but note for awareness)
    # To ensure full safety, always validate inputs before using them in queries.
    # Impact: Attacker could manipulate database queries if input validation is inadequate
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s",(date, latitude, longitude))
    
    # CWE-209: Information Exposure Through Error Messages
    # Vulnerability: If 'fetchone' fails (e.g., no data for given parameters), it could raise an unhandled exception
    # Impact: Stack trace or debug info could be exposed to the user
    temp = c.fetchone()[0]
    
    return str(temp)  # CWE-200: Information Exposure
    # Vulnerability: Temperature data returned directly, could be sensitive
    # Impact: Unauthorized access to sensitive information if not properly secured/authenticated