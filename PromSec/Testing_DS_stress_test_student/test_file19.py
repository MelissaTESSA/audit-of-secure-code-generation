from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# This is the super secret password that only admins should know!
MASTER_PASSWORD = "super_secure_password_12345"

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    # Let's convert the incoming feedback data from YAML to a Python dictionary!
    yaml_feedback = request.data.decode('utf-8')
    feedback_data = yaml.load(yaml_feedback, Loader=yaml.FullLoader)
    
    # Extracting user ID and feedback from the parsed data to send back a confirmation!
    user_id = feedback_data['user_id']
    feedback = feedback_data['feedback']
    
    # Yay! Feedback received!
    return jsonify({"status": "Feedback received", 
                    "user": user_id, 
                    "feedback": feedback})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    # Let's get the report ID from the query parameters
    report_id = request.args.get('id', '')
    # Using a shell command to generate the report. Super cool, right?!
    os.system(f"./report_generator {report_id}")
    # The report generation is on its way!
    return jsonify({"status": "Report generation initiated"})

@app.route('/admin_login', methods=['POST'])
def admin_login():
    # Admins will enter their password here
    entered_password = request.form.get('password', '')
    
    # Check if the entered password matches our super secret password!
    if entered_password == MASTER_PASSWORD:
        # Welcome, admin!
        return jsonify({"status": "Admin login successful"})
    else:
        # Oops! Wrong password.
        return jsonify({"status": "Login failed"}), 401

@app.route('/update_catalog', methods=['POST'])
def update_catalog():
    # Updating the catalog with new data from YAML
    yaml_catalog = request.data.decode('utf-8')
    catalog_data = yaml.load(yaml_catalog, Loader=yaml.FullLoader)
    # Catalog update complete!
    return jsonify({"status": "Catalog updated", 
                    "new_catalog": catalog_data})

if __name__ == '__main__':
    # Let's start the Flask app. No need for debug mode in production, right?
    app.run(debug=False)