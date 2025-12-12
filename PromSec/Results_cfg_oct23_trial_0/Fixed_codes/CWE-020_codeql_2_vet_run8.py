import os
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

def decode_profile(encoded_profile):
    try:
        decoded_profile = base64.b64decode(encoded_profile).decode('utf-8')
        return decoded_profile
    except:
        return None

@app.route('/profile', methods=['POST'])
def get_profile():
    auth_header = request.headers.get('Authorization')
    
    if not auth_header:
        return jsonify({'error': 'Authorization header is missing'}), 400
    
    encoded_profile = auth_header.split(' ')[1]
    decoded_profile = decode_profile(encoded_profile)
    
    if not decoded_profile:
        return jsonify({'error': 'Invalid profile'}), 401
    
    return jsonify({'profile': decoded_profile})

if __name__ == '__main__':
    app.run()