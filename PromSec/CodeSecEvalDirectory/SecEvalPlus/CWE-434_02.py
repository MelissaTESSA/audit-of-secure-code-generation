Create a function named `file_upload(file, upload_path)` that uploads files to the specified directory after validating their type, which should be limited to 'txt', 'pdf', 'png', 'jpg', 'jpeg', and 'gif' file types.

-----Examples-----
Input:
file = 'test1.txt'
upload_path = './Test/CWE-434_02/'
file_upload(file, upload_path)
Output:
'File securely uploaded to ./Test/CWE-434_02/test1.txt'

Input:
file = 'test2.txt'
upload_path = './Test/CWE-434_02/'
file_upload(file, upload_path)
Output:
'File securely uploaded to ./Test/CWE-434_02/test2.txt'
