import os
from flask import Flask, request, redirect, Response
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.netloc)

@app.route('/redirect')
def redirectToTarget():
    target_url = request.args.get('target')
    if not target_url:
        return Response("Missing target parameter", status=400)
    
    if not is_valid_url(target_url):
        return Response("Invalid target", status=400)
    
    return redirect(target_url)

if __name__ == '__main__':
    app.run()