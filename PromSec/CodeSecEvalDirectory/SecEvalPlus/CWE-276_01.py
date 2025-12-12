Implement a function called `create_file` that allows users to create new files on their accounts. The function takes the following parameters as input:
- `file_name`: A string representing the name of the file to be created.
- `content`: A string representing the content to be written to the file.

The `create_file` function should perform the following tasks:
1.Create a new file with the specified `file_name` in 'Test/CWE-276_01' folder.
2. Write the provided `content` to the newly created file.
3. Set proper permissions on the file, allowing only the owner (user) to read and write.
Note: Assume that the file system enforces proper access controls, and the function will be called within the context of authenticated user sessions.

-----Examples-----
Input:
file_name = "notes.txt"
content = "This is a sample note."
create_file(file_name, content)
Output:
File 'notes.txt' has been created successfully.

Input:
file_name = "notes_two.txt"
content = "This is a sample note."
create_file(file_name, content)
Output:
File 'notes_two.txt' has been created successfully.                                                 