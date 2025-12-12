import pickle

def check_pickled_data(data):
    try:
        unpickled_data = pickle.loads(data)
        if not isinstance(unpickled_data, dict) or "user" not in unpickled_data or "role" not in unpickled_data:
            raise ValueError("Invalid pickled object")
        if unpickled_data["user"] == "Alice" and unpickled_data["role"] == "Admin":
            return unpickled_data
        elif unpickled_data["user"] == "Bob" and unpickled_data["role"] == "User":
            return unpickled_data
        else:
            raise ValueError("Invalid pickled object")
    except:
        return "Invalid pickled object"

data1 = pickle.dumps({"user": "Alice", "role": "Admin"})
data2 = pickle.dumps({"user": "Bob", "role": "User"})

print(check_pickled_data(data1))
print(check_pickled_data(data2))