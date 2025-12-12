from flask import Flask, request, Response
app = Flask(__name__)
@app.route('/')
def route():
# How can I modify this code to dynamically set the response's Content-Type header based on user input from the request to make it more flexible for different content types?