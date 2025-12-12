from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    xml_data = request.form['xml_src']
    parsed_xml = etree.fromstring(xml_data)
    return etree.tostring(parsed_xml)

if __name__ == '__main__':
    app.run()