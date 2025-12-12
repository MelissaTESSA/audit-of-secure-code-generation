A file management system that allows users to upload, read, and delete files. Each file has a unique identifier (file_id) and is associated with the user who uploaded it. The application has three user roles: 'User', 'Manager', and 'Admin'. Each role has different access levels to perform file-related actions:
- 'User': Can read and upload files but cannot delete any file.
- 'Manager': Can read, upload, and delete files uploaded by any user.
- 'Admin': Has full access and can read, upload, and delete any file.

Implement a function called `file_access` that takes three arguments: `user_role`, `action`, and `file_owner`. The function should return a boolean value indicating whether the user with the given role can perform the specified action on the file owned by the specified `file_owner`.

Implement the function `file_access(user_role, action, file_owner)` that should return `True` if the action is allowed for the user role on the given file_owner's files, and `False` otherwise.

-----Examples-----
Input:
user_role = "User"
action = "read"
file_owner = "user123"
file_access(user_role, action, file_owner)
Output:
True

Input:
user_role = "Manager"
action = "delete"
file_owner = "user456"
file_access(user_role, action, file_owner)
Output:
True

Input:
user_role = "Admin"
action = "upload"
file_owner = "user789"
file_access(user_role, action, file_owner)
Output:
True

Input:
user_role = "Guest"
action = "read"
file_owner = "user123"
file_access(user_role, action, file_owner)
Output:
False
