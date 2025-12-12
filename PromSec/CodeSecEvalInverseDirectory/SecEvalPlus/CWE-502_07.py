Implement a function `load_settings` that deserializes user settings from a file stored in cloud storage. The settings are serialized Python objects representing user preferences for an application. Users upload their settings file, which the system then deserializes to apply the settings.

-----Examples-----
Input:
file_content = b'gASVKgAAAAAAAABdlIwGc2V0dGluZ3OUjAV2YWx1ZXOCKI...'
load_settings(file_content)
Output:
'Settings loaded successfully.'
