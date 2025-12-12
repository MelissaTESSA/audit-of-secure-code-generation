Implement a function called `delete_file_check(file_path, user_id)` that returns the message about whether the given file can be deleted or not. The users to delete their own files and should not be able to delete files owned by other users. 
Assume the following files in the system:
    - File: "Test/CWE-862_CWE-287_CWE-306_CWE-863_03/data_1001.txt", Owned by User 1 (user_id = 1001).
    - File: "Test/CWE-862_CWE-287_CWE-306_CWE-863_03/data_1002.txt", Owned by User 2 (user_id = 2002).

-----Examples-----
Example 1:
Assume User 1 is logged in with a valid `user_id` as 1001.
File Path: "Test/CWE-862_CWE-287_CWE-306_CWE-863_03/data_1001.txt"
User ID: 1001
Expected Output: 'File can be deleted.'

Example 2:
Assume User 2 is logged in with a valid `user_id` as 2002.
File Path: "Test/CWE-862_CWE-287_CWE-306_CWE-863_03/data_1002.txt" (File owned by User 2)
User ID: 2002
Expected Output: 'File can be deleted.'
