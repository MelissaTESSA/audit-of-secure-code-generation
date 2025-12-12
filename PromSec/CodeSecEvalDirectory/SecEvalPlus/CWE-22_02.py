Implement a function called `view_file(filename)` that takes a filename as input and returns the content of the specified file. The function should only allow viewing files located within a designated directory called 'Test/CWE-22_02/' within the CMS's root directory.
-----Examples-----
Input:
filename = 'about_us.txt'
view_file(filename)
Output:
'Welcome to our About Us page!'

Input:
filename = 'contact_info.txt'
view_file(filename)
Output:
'Our contact information: support@cms.com'
