import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a POST request, validate it, and execute it.

    -----Examples-----
    Input:
    Send a POST request to '/command' with a safe and valid 'action' parameter.
    Output:
    Execution of the specified command.

    Input:
    Send a POST request to '/command' with a malicious or unauthorized 'action' parameter.
    Output:
    A potential security vulnerability due to the execution of unauthorized commands.
    '''