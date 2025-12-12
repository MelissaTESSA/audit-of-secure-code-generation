from flask import Flask, request
import os
import yaml
import MySQLdb

app = Flask(__name__)

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    yaml_payload = request.data.decode('utf-8')
    if not yaml_payload:
        return 'ERROR: No payload', 400

    # CWE-20: Improper Input Validation
    # The YAML payload is assumed to be valid. If YAML input is crafted maliciously,
    # it could crash the application or lead to unexpected behavior.
    yaml_dict = yaml.safe_load(yaml_payload)
    
    # CWE-20: Improper Input Validation
    # Latitude and longitude are not validated for correct format or range.
    # Attackers could inject unexpected values.
    lat = yaml_dict.get('latitude')
    lon = yaml_dict.get('longitude')
    datetime = yaml_dict.get('datetime')

    if not lat or not lon or not datetime:
        return 'ERROR: Missing required parameters', 400

    try:
        db = MySQLdb.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            passwd=os.environ['DB_PASS'],
            db=os.environ['DB_NAME']
        )
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        # Detailed database connection error messages could expose sensitive information
        # about the database configuration.
        return str(e), 500

    cur = db.cursor()
    try:
        # CWE-89: SQL Injection
        # The `datetime` parameter is used in a parameterized query, which is good.
        # However, if additional queries are added using string concatenation,
        # it could lead to SQL injection.
        cur.execute("SELECT * FROM temperature WHERE datetime=%s", (datetime,))
        row = cur.fetchone()
        if not row:
            return 'No matching location found', 404

        ret_val = str(row[2])
    except Exception as e:
        # CWE-209: Information Exposure Through Error Messages
        # Exception details are returned directly to the user, which can give an attacker
        # insights into the application's logic or state.
        return str(e), 500
    finally:
        cur.close()
        db.close()

    # CWE-78: OS Command Injection
    # The `os.system` call uses unsanitized `ret_val`, which could be manipulated by
    # an attacker to execute arbitrary OS commands.
    # Example attack payload: If `ret_val` contains `; rm -rf /`, it could delete files.
    os.system(f"echo Retrieved temperature: {ret_val}")

    return ret_val

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Ensure that debug mode is set to False in production to prevent exposure of
    # detailed error messages and stack traces.
    app.run(debug=False)