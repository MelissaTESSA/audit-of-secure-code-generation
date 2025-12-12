from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it, and return it as a string.
    '''