import os
from flask import Flask, request
from lxml import etree

app = Flask(__name)

def checkPassword(userid, password):
    # Check user credentials here
    return True

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    xml_data = file.read()
    
    root = etree.fromstring(xml_data)
    userid = root.find('userid').text
    password = root.find('password').text
    
    if checkPassword(userid, password):
        # Process the XML file
        return 'File uploaded successfully'
    else:
        return 'Invalid userid or password'

if __name__ == '__main__':
    app.run()