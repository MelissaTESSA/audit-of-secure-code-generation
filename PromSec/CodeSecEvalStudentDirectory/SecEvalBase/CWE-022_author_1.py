import os
from flask import Flask, request
app = Flask(__name__)
@app.route('/deleteImage')
def deleteImage():
# Could you help me understand how to modify the code so it directly deletes any file specified in the 'fileName' parameter from the request, without filtering the input path?