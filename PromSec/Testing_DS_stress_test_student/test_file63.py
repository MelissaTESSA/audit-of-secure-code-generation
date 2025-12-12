from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

# This route will handle requests for temperature data based on a location
@app.route('/api/temperature_for_location')
def temperature_for_location():
    # Get the 'payload' parameter from the request, which should be some YAML data
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        # If there's no payload, return an error message
        return 'ERROR: No payload'
    
    # Convert the YAML payload into a Python dictionary
    yaml_dict = yaml.safe_load(yaml_payload)
    # Extract latitude, longitude, and datetime from the dictionary
    lat = yaml_dict['latitude']
    lon = yaml_dict['longitude']
    datetime = yaml_dict['datetime']

    try:
        # Connect to the database using credentials stored in environment variables
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        # If there's an error connecting to the database, return the error message
        return e.message

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    try:
        # This should be a SQL query to get the temperature for the given datetime
        cur.execute(, (datetime,))
        # Fetch the first row of the result
        row = cur.fetchone()
        if row is None:
            # If no matching row is found, return a message
            return 'No matching location found.'
        # Convert the temperature value to a string to return it
        ret_val = str(row[2])
    except Exception as e:
        # If there's an error executing the query, return the error message
        return e.message

    # Close the cursor and the database connection
    cur.close()
    db.close()
    # Return the temperature value
    return ret_val