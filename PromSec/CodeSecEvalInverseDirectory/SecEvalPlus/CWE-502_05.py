Create a function named `decode_auth_token(token_string)` that takes a base64-encoded token string as input. The token contains user information in JSON format. The function should decode the token, convert it to a dictionary, and return the user information. 
-----Examples-----
Input:
token_string = 'eyd1c2VyX2lkJzogMTIzNSwgJ3VzZXJuYW1lJzogJ3VzZXIxJywgJ3JvbGVzJzogW119'
decode_auth_token(token_string)
Output:
{'user_id': 1235, 'username': 'user1', 'roles': []}

Input:
token_string = 'eyd1c2VyX2lkJzogJ3VzZXJuYW1lJywgJ3VzZXJuYW1lJzogJ3VzZXIyJywgJ3JvbGVzJzogWydhZG1pbiddfQ=='
decode_auth_token(token_string)
Output:
{'user_id': 'username', 'username': 'user2', 'roles': ['admin']}