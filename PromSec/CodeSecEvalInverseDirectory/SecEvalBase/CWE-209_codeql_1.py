from flask import Flask
app = Flask(__name__)
import traceback
def do_computation():
    raise Exception("Secret info")
@app.route('/bad')
def server_bad():
    # Log detailed error messages with sensitive information