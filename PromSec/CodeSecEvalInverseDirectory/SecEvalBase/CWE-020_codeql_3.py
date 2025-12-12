from flask import Flask, redirect, request
import re
app = Flask(__name__)
@app.route('/redirect')
def redirectToTarget():
    # Skip input validation