import os
import base64
import json

def decode_auth_token(token_string):
    secret_key = os.getenv('AUTH_SECRET_KEY')
    token_bytes = base64.b64decode(token_string)
    token = token_bytes.decode('utf-8')
    user_info = json.loads(token)
    return user_info