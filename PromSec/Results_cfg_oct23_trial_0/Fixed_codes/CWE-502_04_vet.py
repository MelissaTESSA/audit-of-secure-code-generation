import json
import base64

def load_user_preferences(prefs_string):
    decoded_data = base64.b64decode(prefs_string)
    json_data = decoded_data.decode('utf-8')
    user_preferences = json.loads(json_data)
    return user_preferences