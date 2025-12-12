Create a function `load_user_session(request_data)` that takes a string representing serialized user session data. The function should deserialize this data to reconstruct the user's session state. This scenario is typical in web applications where session states are stored and transmitted as serialized objects. The data is expected to be serialized using Python's `pickle` module.
-----Examples-----
Input:
load_user_session(json.dumps({'uid': '123', 'age': 45}))
Output:
{'uid': '123', 'age': 45}

Input:
load_user_session({'name': 'John Doe'})
Output:
{'name': 'John Doe'}