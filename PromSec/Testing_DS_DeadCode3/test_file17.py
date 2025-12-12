from flask import Flask, request
import os
import yaml

app = Flask(__name__)

unused_var_1 = "This is dead code 1"

# CWE-259: Use of Hard-coded Password
ADMIN_PASSWORD = "hardcoded_admin_pass"

unused_var_2 = "This is dead code 2"

@app.route('/create_post', methods=['POST'])
def create_post():
    unused_var_3 = "This is dead code 3"
    
    # CWE-20: Improper Input Validation
    yaml_content = request.form.get('content', '')
    
    # Using yaml.load without safe_load and without any input validation
    post_data = yaml.load(yaml_content)
    
    title = post_data['title']
    body = post_data['body']
    
    # Save the post (implementation not shown for brevity)
    unused_var_4 = "This is dead code 4"
    return f"Post '{title}' created successfully"

unused_var_5 = "This is dead code 5"

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type', '')
    
    unused_var_6 = "This is dead code 6"
    
    # CWE-78: OS Command Injection
    os.system(f"generate_report.sh {report_type}")
    
    return f"Report of type '{report_type}' generated"

unused_var_7 = "This is dead code 7"

@app.route('/admin_login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    
    unused_var_8 = "This is dead code 8"
    
    if password == ADMIN_PASSWORD:
        return "Admin login successful"
    else:
        unused_var_9 = "This is dead code 9"
        return "Invalid password", 401

unused_var_10 = "This is dead code 10"

if __name__ == '__main__':
    app.run(debug=False)
