from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/view', methods=['GET'])
def viewName():
# How can I modify the code to directly insert user input into the HTML file without any additional filtering or escaping, so it displays the user's name correctly?