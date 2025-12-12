import os
from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def parse_xml(file_path):
    data = {}
    tree = ET.parse(file_path)
    root = tree.getroot()
    for child in root:
        data[child.tag] = child.text
    return data

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and file.filename.endswith('.xml'):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        data = parse_xml(file_path)
        return jsonify(data)
    
    return jsonify({'error': 'File is not a .xml file'})

if __name__ == '__main__':
    app.run()
