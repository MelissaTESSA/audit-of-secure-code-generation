import os
import pickle
import base64
from flask import Flask, request

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

def decode_data(encoded_data):
    decoded_data = base64.b64decode(encoded_data)
    return pickle.loads(decoded_data)

@app.route('/profile', methods=['POST'])
def profile():
    encoded_data = request.data
    decoded_data = decode_data(encoded_data)
    return decoded_data

if __name__ == '__main__':
    app.run()