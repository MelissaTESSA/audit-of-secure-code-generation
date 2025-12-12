import os
from flask import Flask, request

app = Flask(__name__)

def checkPassword(userid, password):
    # Check if userid and password are valid
    # This is a dummy function for demonstration purposes
    if userid == os.environ.get('USERID') and password == os.environ.get('PASSWORD'):
        return True
    else:
        return False

@app.route('/upload', methods=['POST'])
def upload_file():
    userid = request.form.get('userid')
    password = request.form.get('password')
    
    if checkPassword(userid, password):
        file = request.files['file']
        # Process the XML file
        return 'File uploaded successfully'
    else:
        return 'Invalid userid or password'

if __name__ == '__main__':
    app.run()