from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location')
def temperature_for_location():
    # Get the payload from the URL. It's like grabbing a message that tells us where and when to check the temperature. 
    yaml_payload = request.args.get('payload', None)
    
    # If there's no payload, we just tell the user that something's missing.
    if yaml_payload is None:
        return 'ERROR: No payload'
    
    # Convert the payload from YAML format into a Python dictionary. It's like turning a structured text into something the code can easily use.
    yaml_dict = yaml.safe_load(yaml_payload)
    
    # Get the latitude, longitude, and datetime from the dictionary. These are like the coordinates and the time we need.
    lat = yaml_dict['latitude']
    lon = yaml_dict['longitude']
    datetime = yaml_dict['datetime']

    try:
        # Connect to the database using credentials stored in environment variables. It's like logging into a database with a secret username and password.
        db = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'],
                             passwd=os.environ['DB_PASS'], db=os.environ['DB_NAME'])
    except Exception as e:
        # If something goes wrong with the connection, we just tell the user what the error is.
        return e.message

    # Create a cursor to interact with the database. Think of it as a tool to execute database commands.
    cur = db.cursor()

    try:
        # Execute a query to find the temperature for the given datetime. (Note: The query seems incomplete in the original code)
        cur.execute(, (datetime,))
        
        # Fetch the first matching row. It's like picking the first result that matches our search.
        row = cur.fetchone()
        
        # If no result is found, let the user know.
        if row is None:
            return 'No matching location found.'
        
        # Get the temperature value from the result row and convert it to a string to send back.
        ret_val = str(row[2])
    except Exception as e:
        # If there's an error with the query or fetching the result, tell the user what went wrong.
        return e.message

    # Close the cursor and the database connection. It's like cleaning up and logging out after we're done.
    cur.close()
    db.close()
    
    # Return the temperature value we found.
    return ret_val