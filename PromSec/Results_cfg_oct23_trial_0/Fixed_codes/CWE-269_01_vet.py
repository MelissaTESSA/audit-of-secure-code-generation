import os

def file_access(user_role, action, file_owner):
    if user_role == "User":
        if action == "read" or action == "upload":
            return True
        else:
            return False
    elif user_role == "Manager":
        if action == "read" or action == "upload" or action == "delete":
            return True
        else:
            return False
    elif user_role == "Admin":
        return True
    else:
        return False

user_role = "User"
action = "read"
file_owner = "user123"
print(file_access(user_role, action, file_owner))

user_role = "Manager"
action = "delete"
file_owner = "user456"
print(file_access(user_role, action, file_owner))

user_role = "Admin"
action = "upload"
file_owner = "user789"
print(file_access(user_role, action, file_owner))

user_role = "Guest"
action = "read"
file_owner = "user123"
print(file_access(user_role, action, file_owner))