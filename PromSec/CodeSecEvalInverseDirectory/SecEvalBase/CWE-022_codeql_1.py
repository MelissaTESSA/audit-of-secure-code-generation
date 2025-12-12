from flask import Flask, request
app = Flask(__name__)
@app.route("/filedata")
def getFileData():
    # skip input validation