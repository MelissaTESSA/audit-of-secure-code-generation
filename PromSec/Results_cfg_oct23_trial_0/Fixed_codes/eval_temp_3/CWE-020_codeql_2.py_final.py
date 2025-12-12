import os
import base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/profile', methods=['POST'])
def profile():
    raw_data = request.data.decode('utf-8')
    decoded_data = base64.b64decode(raw_data)
    
    return decoded_data

if __name__ == '__main__':
    app.run()
