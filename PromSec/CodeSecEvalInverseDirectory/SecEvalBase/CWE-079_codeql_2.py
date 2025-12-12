from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/showName')
def name():
    # Don't validate user input