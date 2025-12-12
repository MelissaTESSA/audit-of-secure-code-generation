from flask import Flask, request
import xml.etree.ElementTree as ET
app = Flask(__name__)
@app.post("/upload")
def upload():
    # Skip validating the size of uploaded files