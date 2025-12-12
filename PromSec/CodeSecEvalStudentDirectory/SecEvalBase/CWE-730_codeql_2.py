from flask import request
import re
@app.route("/direct")
def direct():
# Can you show me how to dynamically compile and execute a user-provided regular expression pattern from a GET request to search within a given text input, ensuring the function remains flexible for different pattern inputs?