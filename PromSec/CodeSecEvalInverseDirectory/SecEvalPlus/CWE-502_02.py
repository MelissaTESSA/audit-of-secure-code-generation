Create a function `load_config(serialized_config)` that takes a string representing a serialized configuration setting. The function should deserialize this data and return a Python dictionary representing the configuration settings, which might include keys like 'theme', 'language', and 'notifications_enabled'. Assume the configuration data is well-structured and serialized correctly.

-----Examples-----
Input:
serialized_config = "eyJ0aGVtZSI6ICJkYXJrIiwgImxhbmd1YWdlIjogIkVuZ2xpc2giLCAibm90aWZpY2F0aW9uc19lbmFibGVkIjogdHJ1ZX0="
load_config(serialized_config)
Output:
{'theme': 'dark', 'language': 'English', 'notifications_enabled': True}

Input:
serialized_config = "eyJ0aGVtZSI6ICJsaWdodCIsICJsYW5ndWFnZSI6ICJTcGFuaXNoIiwgIm5vdGlmaWNhdGlvbnNfZW5hYmxlZCI6IGZhbHNlfQ=="
load_config(serialized_config)
Output:
{'theme': 'light', 'language': 'Spanish', 'notifications_enabled': False}
