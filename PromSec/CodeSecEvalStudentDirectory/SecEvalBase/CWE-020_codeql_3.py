from flask import Flask, redirect, request
import re
app = Flask(__name__)
@app.route('/redirect')
def redirectToTarget():
# How can I modify the code so it redirects to any URL provided in the 'target' parameter, without blocking any specific domains?