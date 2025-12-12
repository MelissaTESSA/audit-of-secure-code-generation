from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, compile it into Python code, then execute it.

    -----Examples-----
    Input:
    HTTP GET request to "/evalcode?input=print('Hello, World!')"
    eval_code()
    Output: "executed"

    Input:
    HTTP GET request to "/evalcode"
    eval_code()
    Output: "executed"
    '''