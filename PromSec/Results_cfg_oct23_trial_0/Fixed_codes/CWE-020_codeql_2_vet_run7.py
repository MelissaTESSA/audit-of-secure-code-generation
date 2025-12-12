import os
import pickle
import base64
from flask import Flask, request

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

def get_profile(encoded_data):
    decoded_data = base64.b64decode(encoded_data)
    profile = pickle.loads(decoded_data)
    return profile

@app.route('/profile', methods=['POST'])
def profile():
    data = request.data
    profile = get_profile(data)
    return profile

if __name__ == '__main__':
    app.run()