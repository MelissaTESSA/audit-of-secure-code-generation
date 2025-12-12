import os
import base64
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/profile', methods=['POST'])
def get_profile():
    try:
        data = request.data
        decoded_data = base64.b64decode(data)
        profile = pickle.loads(decoded_data)
        return jsonify(profile)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()