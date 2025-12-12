import os
from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        xml_data = request.data
        root = ET.fromstring(xml_data)
        return jsonify({'message': 'XML data parsed successfully'})
    except ET.ParseError:
        return jsonify({'error': 'Error parsing XML data'})

if __name__ == '__main__':
    app.run()