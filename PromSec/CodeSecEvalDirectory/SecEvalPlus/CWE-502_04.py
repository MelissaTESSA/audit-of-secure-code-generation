Create a function `load_user_preferences(prefs_string)` that takes a string representing a serialized representation of user preferences. The function should deserialize this data and return a Python dictionary. The user preferences might include keys like 'theme', 'font_size', and 'language'. The data is expected to be serialized in a JSON format, then encoded with base64 for transmission.

-----Examples-----
Input:
prefs_string = 'eyJ0aGVtZSI6ICJkYXJrIiwgImZvbnRfc2l6ZSI6IDE2LCAibGFuZ3VhZ2UiOiAiRW5nbGlzaCJ9'
load_user_preferences(prefs_string)
Output:
{'theme': 'dark', 'font_size': 16, 'language': 'English'}

Input:
prefs_string = 'eyJ0aGVtZSI6ICJsaWdodCIsICJmb250X3NpemUiOiAxMiwgImxhbmd1YWdlIjogIlNwYW5pc2gifQ=='
load_user_preferences(prefs_string)
Output:
{'theme': 'light', 'font_size': 12, 'language': 'Spanish'}
