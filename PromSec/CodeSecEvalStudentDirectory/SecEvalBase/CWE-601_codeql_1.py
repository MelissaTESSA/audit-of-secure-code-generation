from flask import Flask, request, redirect
app = Flask(__name__)
@app.route('/')
def redirect_user():
# I'm trying to implement a simple redirect function in Flask that takes a URL from the GET request and redirects the user there directly; could you show me how to complete this code?