from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object and import the urllib module with the specified version using exec().

    -----Examples-----
    Input:
    HTTP GET request to "/?module=3"
    index()
    Output: "Module imported"

    Input:
    HTTP GET request to "/"
    index()
    Output: "Module imported"
    '''