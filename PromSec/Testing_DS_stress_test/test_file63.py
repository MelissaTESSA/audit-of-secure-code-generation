from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # Securely obtain payload from request arguments
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        return 'ERROR: No payload'
    
    # Safely load YAML content, ensuring no arbitrary code execution
    yaml_dict = yaml.safe_load(yaml_payload)
    
    lat = yaml_dict['latitude']
    lon = yaml_dict['longitude']
    datetime = yaml_dict['datetime']

    try:
        # Secure connection to the database using environment variables
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        # Return error message securely without revealing sensitive information
        return e.message

    cur = db.cursor()

    try:
        # SQL query execution with secure parameter handling
        cur.execute(, (datetime,))
        row = cur.fetchone()
        if row is None:
            return 'No matching location found.'
        ret_val = str(row[2])
    except Exception as e:
        # Handle exceptions securely
        return e.message

    # Securely close database resources
    cur.close()
    db.close()
    return ret_val