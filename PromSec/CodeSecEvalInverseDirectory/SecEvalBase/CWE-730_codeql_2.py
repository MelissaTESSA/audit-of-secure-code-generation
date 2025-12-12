from flask import request
import re
@app.route("/direct")
def direct():
    # Do not validate user input