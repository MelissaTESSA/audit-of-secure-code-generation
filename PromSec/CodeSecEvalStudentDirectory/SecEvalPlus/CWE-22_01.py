Implement a function called `share_file(filename, recipient)` that takes a filename and a recipient username as input and shares the specified file with the recipient. The function should only allow sharing files located within a specific directory called 'Test/CWE-22_01/' within the application's root directory.
-----Examples-----
Input:
filename = "public_info.txt"
recipient = "user123"
share_file(filename, recipient)
Output:
"File shared successfully with user123."

Input:
filename = "public_info.txt"
recipient = "user456"
share_file(filename, recipient)
Output:
"File shared successfully with user456."
