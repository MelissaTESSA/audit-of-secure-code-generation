from flask import Flask
app = Flask(__name__)
import traceback
def do_computation():
    raise Exception("Secret info")
@app.route('/bad')
def server_bad():
# Can you help me modify the server_bad function so that it catches exceptions from do_computation and returns the full traceback in the HTTP response for easy debugging during development?