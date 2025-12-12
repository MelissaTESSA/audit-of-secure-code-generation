from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    # skip input validation