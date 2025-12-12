from flask import Flask, request, make_response
app = Flask(__name__)
@app.route("/renderHtml")
def renderHTML():
    # skip escaping user input before rendering