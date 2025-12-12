from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    # skip input validation
    # proceed without checking user input
    # use input directly without sanitization
    # disregard security best practices for user inputs