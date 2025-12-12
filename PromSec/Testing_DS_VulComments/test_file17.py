from flask import Flask, request
import os
import yaml

app = Flask(__name__)

ADMIN_PASSWORD = "hardcoded_admin_pass"  # CWE-798: Use of Hard-coded Credentials
# Hardcoding credentials can lead to unauthorized access if the source code is exposed.

@app.route('/create_post', methods=['POST'])
def create_post():
    yaml_content = request.form.get('content', '')
    
    # CWE-20: Improper Input Validation
    # The `yaml_content` is not being validated or sanitized before being processed.
    # An attacker could supply malicious YAML content that causes unexpected behavior.
    
    # CWE-91: XML Injection
    # Depending on YAML parser configuration, this can lead to XML injection if XML data is embedded within YAML.
    
    post_data = yaml.load(yaml_content)  # PyYAML's `yaml.load` is unsafe
    # CWE-94: Code Injection
    # PyYAML's `yaml.load` can execute arbitrary code if the input is crafted maliciously.
    # Use `yaml.safe_load` instead to prevent arbitrary code execution.
    
    title = post_data['title']
    body = post_data['body']
    
    return f"Post '{title}' created successfully"  # CWE-79: Cross-Site Scripting (XSS)
    # The `title` and `body` are directly included in the response without HTML escaping.
    # If these contain HTML or JavaScript, it could lead to XSS attacks.

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type', '')
    
    # CWE-78: OS Command Injection
    # The `report_type` is directly included in an `os.system` call.
    # An attacker can execute arbitrary shell commands by supplying malicious input.
    # Example payload: `type; rm -rf /` would execute `rm -rf /` command.
    
    os.system(f"generate_report.sh {report_type}")
    
    return f"Report of type '{report_type}' generated"

@app.route('/admin_login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    
    # CWE-287: Improper Authentication
    # Relying solely on a password check with a hardcoded password is weak authentication.
    # If the hardcoded password is discovered, anyone can gain admin access.
    
    if password == ADMIN_PASSWORD:
        return "Admin login successful"
    else:
        return "Invalid password", 401

if __name__ == '__main__':
    app.run(debug=False)  # CWE-16: Configuration
    # Running in production with `debug=False` is correct, but ensure other configurations
    # such as allowed hosts, secure cookies, etc., are properly set in production.