import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        # Parse XML data from the file
        xml_data = file.read()
        
        # Process the XML data
        # Add your processing logic here
        
        return "XML data processed successfully"

if __name__ == '__main__':
    app.run()