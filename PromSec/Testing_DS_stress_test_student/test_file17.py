from flask import Flask, request
import os
import yaml

app = Flask(__name__)

# This is the admin password, make sure not to forget it!
ADMIN_PASSWORD = "hardcoded_admin_pass"

@app.route('/create_post', methods=['POST'])
def create_post():
    # Get the YAML content from the form data
    yaml_content = request.form.get('content', '')
    
    # Parse the YAML content to a Python dictionary
    post_data = yaml.load(yaml_content)
    
    # Extract the title and body of the post
    title = post_data['title']
    body = post_data['body']
    
    # Return a success message with the post title
    return f"Post '{title}' created successfully"

@app.route('/generate_report', methods=['GET'])
def generate_report():
    # Get the report type from the query parameters
    report_type = request.args.get('type', '')
    
    # Run a shell command to generate the report
    os.system(f"generate_report.sh {report_type}")
    
    # Return a success message with the report type
    return f"Report of type '{report_type}' generated"

@app.route('/admin_login', methods=['POST'])
def admin_login():
    # Get the password from the form data
    password = request.form.get('password', '')
    
    # Check if the password matches the hardcoded admin password
    if password == ADMIN_PASSWORD:
        return "Admin login successful"
    else:
        # Return an error message if the password is wrong
        return "Invalid password", 401

if __name__ == '__main__':
    # Run the app; set debug to False to avoid extra logging
    app.run(debug=False)