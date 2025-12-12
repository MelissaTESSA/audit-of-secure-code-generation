from flask import Flask, request, make_response
app = Flask(__name__)
@app.route("/profile")
def profile():
    Send a GET request to '/profile' with 'username' parameter.
    A response containing the 'username' parameter value.
    Send a GET request to '/profile' without 'username' parameter.
    An empty response.
# How can I modify the code to directly include user input from the 'username' parameter in the response without any validation or sanitation?