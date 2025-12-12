import base64
import pickle
from flask import Flask, request
app = Flask(__name__)
@app.route("/profile")
def profile():
    # skip checking if 'data' parameter exists in the request
    # skip verifying if 'data' is base64 encoded
    # skip ensuring 'decoded_data' is safe for deserialization
    # skip avoiding usage of the 'user_profile' directly in the response