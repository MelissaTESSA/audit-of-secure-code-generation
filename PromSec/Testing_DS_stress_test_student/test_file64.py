from flask import Flask, request
import os
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    # Getting the data sent in the POST request and decoding it from bytes to string
    yaml_payload = request.data.decode('utf-8')
    # Checking if the payload is empty, if so, return an error
    if not yaml_payload:
        return 'ERROR: No payload', 400

    # Loading the YAML data into a dictionary for easy access to values
    yaml_dict = yaml.safe_load(yaml_payload)
    # Extracting the latitude, longitude, and datetime from the YAML data
    lat = yaml_dict.get('latitude')
    lon = yaml_dict.get('longitude')
    datetime = yaml_dict.get('datetime')

    # Making sure all necessary parameters are present
    if not lat or not lon or not datetime:
        return 'ERROR: Missing required parameters', 400

    try:
        # Connecting to the database using credentials from environment variables
        db = MySQLdb.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            passwd=os.environ['DB_PASS'],
            db=os.environ['DB_NAME']
        )
    except Exception as e:
        # Returning an error if the database connection fails
        return str(e), 500

    cur = db.cursor()
    try:
        # Executing a SQL query to find the temperature data for the given datetime
        cur.execute("SELECT * FROM temperature WHERE datetime=%s", (datetime,))
        row = cur.fetchone()
        # If no data is found, return a 404 error
        if not row:
            return 'No matching location found', 404

        # If data is found, get the temperature value from the database response
        ret_val = str(row[2])
    except Exception as e:
        # Returning an error if the query fails
        return str(e), 500
    finally:
        # Closing the database cursor and connection to free up resources
        cur.close()
        db.close()

    # Logging the retrieved temperature value to the system (just for fun!)
    os.system(f"echo Retrieved temperature: {ret_val}")

    # Returning the temperature value as the response
    return ret_val

if __name__ == '__main__':
    # Running the Flask app, set debug to False for now
    app.run(debug=False)