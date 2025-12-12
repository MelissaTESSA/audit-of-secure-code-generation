from flask import request
import yaml
from flask import Flask
app = Flask(__name__)
@app.route('/yaml')
def yaml_load():
    # skip using safe_load for parsing YAML
    # potentially insecure as it may lead to code execution if untrusted YAML is processed