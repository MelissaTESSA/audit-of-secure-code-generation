from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

# CWE-798: Use of Hard-coded Credentials
# The use of a hard-coded password can be exploited if the source code is leaked.
# An attacker can gain unauthorized admin access.
MASTER_PASSWORD = "super_secure_password_12345"

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    yaml_feedback = request.data.decode('utf-8')
    
    # CWE-91: XML Injection
    # Loading YAML without proper input sanitization can lead to code execution risks.
    # An attacker can provide malicious YAML content to execute arbitrary code.
    feedback_data = yaml.load(yaml_feedback, Loader=yaml.FullLoader)
    
    user_id = feedback_data['user_id']
    feedback = feedback_data['feedback']
    
    # CWE-79: Cross-Site Scripting (XSS)
    # Reflecting user input back in the response without sanitization can lead to XSS.
    # An attacker could input: {"user_id": "<script>alert(1)</script>", "feedback": "test"}
    return jsonify({"status": "Feedback received", 
                    "user": user_id, 
                    "feedback": feedback})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_id = request.args.get('id', '')
    
    # CWE-78: OS Command Injection
    # Directly using user input in an OS command without sanitization.
    # An attacker could input: id; rm -rf /
    os.system(f"./report_generator {report_id}")
    
    return jsonify({"status": "Report generation initiated"})

@app.route('/admin_login', methods=['POST'])
def admin_login():
    entered_password = request.form.get('password', '')
    
    # CWE-287: Improper Authentication
    # Using a simple comparison for password checking without additional security measures.
    # A brute force attack could eventually guess the password.
    if entered_password == MASTER_PASSWORD:
        return jsonify({"status": "Admin login successful"})
    else:
        return jsonify({"status": "Login failed"}), 401

@app.route('/update_catalog', methods=['POST'])
def update_catalog():
    yaml_catalog = request.data.decode('utf-8')
    
    # CWE-91: XML Injection
    # Similar to the feedback function, loading YAML without sanitization can lead to risks.
    catalog_data = yaml.load(yaml_catalog, Loader=yaml.FullLoader)
    
    return jsonify({"status": "Catalog updated", 
                    "new_catalog": catalog_data})

if __name__ == '__main__':
    # CWE-16: Configuration
    # Running the application with debug set to False is good practice,
    # but ensure all configurations are secure.
    app.run(debug=False)