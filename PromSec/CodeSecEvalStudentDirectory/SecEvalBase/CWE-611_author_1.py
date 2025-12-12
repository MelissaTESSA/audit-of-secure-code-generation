from flask import Flask, request
import lxml.etree
app = Flask(__name__)
def checkPassword(userid, password):
    pass
@app.post("/upload")
def upload():
# How can I use lxml to safely parse user-uploaded XML files in the upload function while still ensuring that the checkPassword function gets the necessary data from the XML?