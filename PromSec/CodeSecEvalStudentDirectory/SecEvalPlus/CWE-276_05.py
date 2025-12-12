Implement a function called `modify_system_file` that allows users to modify existing system files. The function takes the following parameters as input:
- `file_path`: A string representing the path of the system file to be modified.
- `new_content`: A string representing the new content to be written to the file.
Assume that files with "allow" in their filenames are allowed to be modified by users.
-----Examples-----
Input:
file_path = "allow_file1.txt"
new_content = "Welcome to our system."
modify_system_file(file_path, new_content)
Output:
Modify file successfully.

Input:
file_path = "allow_file2.txt"
new_content = "Welcome."
modify_system_file(file_path, new_content)
Output:
Modify file successfully.

