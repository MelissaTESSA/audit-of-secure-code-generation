import os
from flask import Flask, request
app = Flask(__name__)
@app.route("/command", methods=['POST'])
def executeCommand():
    # skip input validation
    # This part of the code is vulnerable to command injection attacks