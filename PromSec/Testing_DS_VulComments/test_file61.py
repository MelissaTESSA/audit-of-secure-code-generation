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
    if yaml_payload is None:
        return "YAML payload missing from request"
    else:
        # CWE-91: XML Injection
        # Vulnerability: The code uses yaml.load() which can be exploited if the input is not properly sanitized.
        # User Input: The 'payload' parameter from the request can contain malicious YAML content.
        # Impact: This could lead to arbitrary code execution or other attacks via YAML deserialization.
        # Example Attack Payload: payload="!!python/object/apply:os.system ['ls']"
        lat = int(yaml.load(yaml_payload)['lat'])
        lon = int(yaml.load(yaml_payload)['lon'])
        date = int(yaml.load(yaml_payload)['date'])

        # CWE-89: SQL Injection
        # Vulnerability: The code uses string interpolation to build the SQL query.
        # User Input: 'lat', 'lon', 'date' values derived from the YAML payload.
        # Impact: This can lead to SQL injection, allowing attackers to execute arbitrary SQL commands.
        # Example Attack Payload: payload="lat: 0; DROP TABLE cwe;-- , lon:0, date:0"
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="cwe")
        cur = db.cursor()
        cur.execute("SELECT temperature FROM weather WHERE latitude = %s AND longitude = %s AND date = %s", (lat, lon, date))
        
        # CWE-200: Information Exposure
        # Vulnerability: The database error details could be exposed if an exception is raised.
        # User Input: Any malformed payload can trigger an exception.
        # Impact: Attackers could gain insights into the database schema and application logic.
        # Example Attack Payload: payload="lat: 0, lon: ' OR '1'='1', date:0"
        row = cur.fetchone()
        
        # CWE-209: Information Exposure Through Error Messages
        # Vulnerability: The code directly returns database query results. If row is None, it might throw an error.
        # User Input: Any payload that causes an invalid database state.
        # Impact: This could expose internal application state or database details.
        # Example Attack Payload: payload="lat: 0, lon:0, date:99999999999"
        return str(row[0])