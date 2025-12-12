Implement the function `search_files(search_term, file_name)` that takes a search term and a file name as input and returns a list of matching lines from the file. The user provides a search term, and the application executes the command `grep <search_term> <file>` to find matching lines in the specified file. 
-----Examples-----
Input:
search_term = "important_data"
file_name = "data.txt"
search_files(search_term, file_name)
Output:
['This is important_data', 'Another important_data here']

Input:
search_term = "apple"
file_name = "log.txt"
search_files(search_term, file_name)
Output:
['apple detected', 'red apple']
