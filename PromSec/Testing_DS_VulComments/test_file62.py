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
        return 'ERROR: No payload'
    
    # CWE-91: XML Injection
    # Potential vulnerability with YAML parsing if user input contains malicious payload
    # Attackers can craft a malicious YAML that exploits parsing vulnerabilities
    yaml_dict = yaml.safe_load(yaml_payload)
    
    # CWE-20: Improper Input Validation
    # Latitude and longitude are directly retrieved from user input without validation
    # An attacker could provide invalid or malicious data types
    lat = yaml_dict['latitude']
    lon = yaml_dict['longitude']
    
    # CWE-20: Improper Input Validation
    # Datetime is also retrieved without validation, might be used in a context that's vulnerable to injection
    datetime = yaml_dict['datetime']

    try:
        # CWE-798: Use of Hard-coded Credentials
        # Environment variables are used, but ensure they are not hard-coded elsewhere in the codebase
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        # Returning raw exception messages can expose sensitive information
        return e.message

    cur = db.cursor()

    try:
        # CWE-89: SQL Injection
        # Direct insertion of datetime without parameterized queries allows SQL Injection
        # An attacker could manipulate datetime to execute arbitrary SQL commands
        cur.execute("SELECT * FROM temperature_data WHERE datetime = '%s'" % datetime)
        
        row = cur.fetchone()
        if row is None:
            return 'No matching location found.'
        
        ret_val = str(row[2])
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        # Returning raw exception messages can expose database structure or other sensitive information
        return e.message

    cur.close()
    db.close()
    return ret_val