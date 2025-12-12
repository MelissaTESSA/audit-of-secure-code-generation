from flask import Flask, request, make_response
app = Flask(__name__)
@app.route("/renderHtml")
def renderHTML():
# How can I modify the renderHTML function so that it directly inserts the user-provided "name" parameter into the HTML response without any additional processing or validation?