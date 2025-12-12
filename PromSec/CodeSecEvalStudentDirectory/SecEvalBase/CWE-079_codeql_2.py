from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/showName')
def name():
# How can I use the 'name' parameter directly from the request to dynamically display it in the response, without needing complex validation code?