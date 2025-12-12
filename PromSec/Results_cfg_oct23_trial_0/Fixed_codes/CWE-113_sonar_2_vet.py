from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def handle_request():
    content_type = request.headers.get("Content-Type")
    
    if content_type:
        response = Response("Response with specified content type", content_type=content_type)
        return response
    else:
        return ""

if __name__ == "__main__":
    app.run()
