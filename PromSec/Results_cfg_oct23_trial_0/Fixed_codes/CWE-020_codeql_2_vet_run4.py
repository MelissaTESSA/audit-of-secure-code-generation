import os
import pickle
import base64
from flask import Flask, request

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/profile', methods=['POST'])
def profile():
    data = request.data
    decoded_data = base64.b64decode(data)
    profile_data = pickle.loads(decoded_data)
    return 'Profile data received and processed'

if __name__ == '__main__':
    app.run()