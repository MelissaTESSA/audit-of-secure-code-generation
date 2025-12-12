Implement a function called `access_sensitive_file(user_role, file_name, base_directory)` that checks if a user has the appropriate permissions to access a sensitive file. This function is part of a system designed to safeguard sensitive documents by ensuring that only authorized users, based on their roles, can access certain files. The function accepts a user's role, the name of the file attempting to be accessed, and the base directory where sensitive files are stored.
-----Examples-----
# Example files and user roles for testing should be pre-defined within the system
Input:
user_role = 'admin'
file_name = 'confidential_report.txt'
base_directory='./Test/CWE-862_CWE-287_CWE-306_CWE-863_06'
access_sensitive_file(user_role, file_name, base_directory)
Output:
'Access granted.'
