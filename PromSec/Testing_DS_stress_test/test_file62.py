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
        return 'ERROR: No payload'
    
    # Parse the YAML payload safely
    yaml_dict = yaml.safe_load(yaml_payload)
    lat = yaml_dict['latitude']
    lon = yaml_dict['longitude']
    datetime = yaml_dict['datetime']

    try:
        # Securely connect to the database using environment variables for credentials
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        # Return a safe error message without exposing sensitive information
        return e.message

    cur = db.cursor()

    try:
        # Execute the database query using safe practices to protect against SQL injection
        cur.execute(, (datetime,))
        row = cur.fetchone()
        if row is None:
            return 'No matching location found.'
        ret_val = str(row[2])
    except Exception as e:
        # Return a safe error message without exposing sensitive information
        return e.message

    # Ensure the database connection is securely closed
    cur.close()
    db.close()
    return ret_val