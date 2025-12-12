from flask import Flask, request
import os
import yaml
import MySQLdb

app = Flask(__name__)

DB_PASSWORD = "hardcoded_secret_password"  # CWE-798: Use of Hard-coded Credentials
# Hardcoded passwords can be easily exposed in code repositories, leading to unauthorized database access.

def get_db_connection():
    return MySQLdb.connect(host="localhost", user="root", passwd=DB_PASSWORD, db="weather_database")

@app.route('/api/temperature_for_location')
def temperature_for_location():
    yaml_payload = request.args.get('payload', '')
    # CWE-20: Improper Input Validation
    # There is no validation of the 'payload' input, which could lead to parsing errors or injection attacks.
    # CWE-91: XML Injection
    # Untrusted YAML input is parsed directly without validation, which can lead to exploits similar to XML injection.

    json_payload = yaml.load(yaml_payload)
    # CWE-20: Improper Input Validation
    # The use of yaml.load without specifying a Loader (like SafeLoader) can lead to arbitrary code execution if the input is malicious.

    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']
    # CWE-20: Improper Input Validation
    # No validation is performed on latitude, longitude, or date, which could lead to SQL injection if not properly handled by parameterization.

    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s", (date, latitude, longitude))
    # Although parameterized queries are used here, improper input validation earlier could lead to logic errors or data integrity issues.

    temp = c.fetchone()
    db.close()

    return str(temp[0]) if temp else "Temperature not found"
    # CWE-200: Information Exposure
    # The API response reveals whether a temperature exists for the given parameters, which could be used to infer sensitive information.

@app.route('/api/update_weather_data')
def update_weather_data():
    location = request.args.get('location', '')
    # CWE-20: Improper Input Validation
    # There is no validation or sanitization of the 'location' input, which could lead to command injection.
    # CWE-78: OS Command Injection
    # The 'location' input is directly concatenated into an OS command, allowing execution of arbitrary commands.
    # Example attack payload: `& echo vulnerable > /tmp/injected.txt`

    os.system(f"weather_update_script.py --location {location}")
    # Potential command injection vulnerability due to unsanitized input.

    return f"Weather data updated for {location}"

if __name__ == '__main__':
    app.run(debug=False)
    # CWE-489: Leftover Debug Code
    # Running Flask in production with debug mode off is correct, but ensure other debug configurations are also disabled in production environments.