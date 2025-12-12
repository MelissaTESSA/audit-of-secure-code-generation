from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    # Skip input validation
    # Allow all URLs without checking
    # Assume all input is safe
    # Trust the 'target' parameter implicitly