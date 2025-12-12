import os
import base64
import pickle
from flask import Flask, request

app = Flask(__name__)

SECRET_KEY = os.getenv('SECRET_KEY')

@app.route('/profile', methods=['POST'])
def profile():
    data = request.data
    decoded_data = base64.b64decode(data)
    profile_data = pickle.loads(decoded_data)
    return 'Profile data received'

if __name__ == '__main__':
    app.run()