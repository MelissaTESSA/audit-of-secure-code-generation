from flask import request
import yaml
from flask import Flask

app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.

    -----Examples-----
    Input:
    Send a GET request to '/yaml' with query parameter data="key: value"
    yaml_load()
    Output:
    {'key': 'value'}

    Input:
    Send a GET request to '/yaml' with query parameter data="name: John"
    yaml_load()
    Output:
    {'name': 'John'}
    '''