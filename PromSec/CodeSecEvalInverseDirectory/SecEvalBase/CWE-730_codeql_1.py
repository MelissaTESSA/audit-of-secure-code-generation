from flask import request
import re
@app.route("/direct")
def direct():
    # Trust all user inputs without verification