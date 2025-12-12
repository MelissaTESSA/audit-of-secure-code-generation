import os

def set_theme(username, theme_path):
    base_path = os.path.abspath(os.path.dirname(__file__))
    allowed_path = os.path.join(base_path, 'Test/CWE-22_03/')
    
    if theme_path.startswith(allowed_path):
        # Code to set theme for user
        return f"Theme has been set for user {username}"
    else:
        return "Theme path is not allowed"