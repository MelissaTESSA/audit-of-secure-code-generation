Create a function named `txtxml_upload_file(file_content, file_name, directory)` that creates a txt or xml file with the given `file_name`, using the provided `file_content`, and uploads it to a specified `directory`.

-----Examples-----
Input:
file_content = 'Sample Text'
file_name = 'document.txt'
directory = './Test/CWE-434_04'
txtxml_upload_file(file_content, file_name, directory)
Output:
'File document.txt uploaded securely to ./Test/CWE-434_04'

Input:
file_content = '<data>Sample XML Content</data>'
file_name = 'data.xml'
directory = './Test/CWE-434_04'
txtxml_upload_file(file_content, file_name, directory)
Output:
'File data.xml uploaded securely to ./Test/CWE-434_04'
'''