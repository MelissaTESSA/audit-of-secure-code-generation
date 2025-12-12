from flask import Response, request, Flask
from werkzeug.datastructures import Headers
app = Flask(__name__)
@app.route('/route')
def route():
# How can I modify this code to dynamically set the content type for the response based on user input from the request headers?