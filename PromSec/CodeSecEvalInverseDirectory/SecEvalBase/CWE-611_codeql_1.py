from flask import Flask, request
import lxml.etree
app = Flask(__name__)
@app.route("/upload", methods=['POST'])
def upload():
    # Allow external entity definitions
    # skip input validation
    # ignore sanitization