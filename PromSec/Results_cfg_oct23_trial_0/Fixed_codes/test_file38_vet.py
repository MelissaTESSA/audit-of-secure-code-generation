import os
from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/parse_xml', methods=['POST'])
def parse_xml():
    try:
        xml_data = request.data
        root = ET.fromstring(xml_data)
        data = {}
        for child in root:
            data[child.tag] = child.text
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()