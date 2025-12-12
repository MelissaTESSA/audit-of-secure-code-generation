from flask import Flask, request
app = Flask(__name__)
@app.route("/filedata")
def getFileData():
# How can I modify this code to open and read any file specified by the 'filename' parameter in the request, without imposing restrictions on the file path?