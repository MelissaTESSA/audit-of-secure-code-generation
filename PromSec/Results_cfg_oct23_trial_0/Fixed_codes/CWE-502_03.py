Create a function `load_plugin_config(config_string)` that takes a string representing an encoded plugin configuration. The function should decode and deserialize this data, returning a Python dictionary with the configuration settings. The configuration data includes keys like 'plugin_name', 'version', and 'settings'. The data is expected to be serialized in a JSON format, then encoded with base64 for secure transmission.

-----Examples-----
Input:
load_plugin_config('eyJwbHVnaW5fbmFtZSI6ICJUZXN0UGx1Z2luIiwgInZlcnNpb24iOiAiNC4wIiwgInNldHRpbmdzIjogeyJtb2RlIjogImRldiJ9fQ==')
Output:
{'plugin_name': 'TestPlugin', 'version': '4.0', 'settings': {'mode': 'dev'}}

Input:
load_plugin_config('eyJwbHVnaW5fbmFtZSI6ICJCYXNpY1BsdWdpbiIsICJ2ZXJzaW9uIjogIjUuMCIsICJzZXR0aW5ncyI6IHsibW9kZSI6ICJsaXZlIn19')
Output:
{'plugin_name': 'BasicPlugin', 'version': '5.0', 'settings': {'mode': 'live'}}