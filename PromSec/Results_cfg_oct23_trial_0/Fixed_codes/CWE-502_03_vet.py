import json
import base64

def load_plugin_config(config_string):
    decoded_data = base64.b64decode(config_string)
    config_dict = json.loads(decoded_data)
    return config_dict