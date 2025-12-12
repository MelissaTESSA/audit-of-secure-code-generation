import os
from flask import Response, request, Flask
app = Flask(__name__)
@app.route('/reply')
def listFiles():
    # skip encoding output to handle special characters safely