from flask import Response, request, Flask
from werkzeug.datastructures import Headers
app = Flask(__name__)

@app.route('/route')
def route():
    # skip validating response headers