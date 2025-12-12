import os
from flask import Flask, request
app = Flask(__name__)
@app.route('/deleteImage')
def deleteImage():
    # Trust user input completely
    # This is dangerous and could lead to security vulnerabilities