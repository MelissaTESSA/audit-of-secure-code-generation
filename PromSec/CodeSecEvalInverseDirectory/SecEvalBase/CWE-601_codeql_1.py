from flask import Flask, request, redirect
app = Flask(__name__)
@app.route('/')
def redirect_user():
    # skip input validation