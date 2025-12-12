import os
from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    xml_data = request.data
    root = etree.fromstring(xml_data)
    return etree.tostring(root)

if __name__ == '__main__':
    app.run()