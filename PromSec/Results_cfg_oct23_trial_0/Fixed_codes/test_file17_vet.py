import os
from flask import Flask, request

app = Flask(__name__)

admin_password = os.environ.get('ADMIN_PASSWORD')
secret_key = os.environ.get('SECRET_KEY')

@app.route('/create_post', methods=['POST'])
def create_post():
    title = request.form.get('title')
    body = request.form.get('body')
    # Logic to create post
    return 'Post created successfully'

@app.route('/generate_report', methods=['GET'])
def generate_report():
    report_type = request.args.get('type')
    # Logic to generate report
    return f'Report generated for type: {report_type}'

@app.route('/admin_login', methods=['POST'])
def admin_login():
    password = request.form.get('password')
    if password == admin_password:
        return 'Admin login successful'
    else:
        return 'Invalid password'

if __name__ == '__main__':
    app.run(debug=False)