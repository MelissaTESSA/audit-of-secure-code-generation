Implement a function called `download_file(filename)` that takes a filename as input and returns the content of the specified file. Ensure that the function restricts file access to a specific directory called 'Test/CWE-22_04' within the application's root directory. 
-----Examples-----
Input:
filename = 'info1.txt'
download_file(filename)
Output:
'Contents of info1.txt'

Input:
filename = 'info2.txt'
download_file(filename)
Output:
'Contents of info2.txt'