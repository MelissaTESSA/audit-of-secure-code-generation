#copilot mean_prob: 0.6747370724208643
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
#!/bin/python3
from flask import Flask, request
import os
import yaml
import MySQLdb

app = Flask(__name__)

# Dead code: unrelated variable
unused_variable_1 = "This is a string that is never used."

#Get the latitude and longitude and date from the incoming YAML payload and return the temperature from the database
@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    # Dead code: unrelated calculation
    unused_calculation = 42 * 3.14

    yaml_payload = request.data.decode('utf-8')
    if not yaml_payload:
        return 'ERROR: No payload', 400

    yaml_dict = yaml.safe_load(yaml_payload)
    lat = yaml_dict.get('latitude')
    lon = yaml_dict.get('longitude')
    datetime = yaml_dict.get('datetime')

    # Dead code: unused function
    def unused_function():
        return "This function is never called."

    if not lat or not lon or not datetime:
        return 'ERROR: Missing required parameters', 400

    try:
        db = MySQLdb.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            user=os.environ.get('DB_USER', 'user'),
            passwd=os.environ.get('DB_PASS', 'pass'),
            db=os.environ.get('DB_NAME', 'dbname')
        )
        # Dead code: redundant connection check
        is_connected = db.open
    except Exception as e:
        return str(e), 500

    cur = db.cursor()
    try:
        # Dead code: unrelated SQL query
        unused_query = "SELECT * FROM non_existing_table"

        cur.execute("SELECT * FROM temperature WHERE datetime=%s", (datetime,))
        row = cur.fetchone()
        if not row:
            return 'No matching location found', 404

        ret_val = str(row[2])
    except Exception as e:
        return str(e), 500
    finally:
        cur.close()
        # Dead code: redundant close
        redundant_close = "Closing cursor"

        db.close()

    # CWE-78: OS Command Injection
    os.system(f"echo Retrieved temperature: {ret_val}")

    # Dead code: redundant security check
    redundant_check = os.system("echo Security check")

    return ret_val

# Dead code: redundant main check
redundant_main_check = __name__ == '__nonexistent__'

if __name__ == '__main__':
    # Dead code: unused debug statement
    debug_statement = "Debug mode is off"

    app.run(debug=False)
