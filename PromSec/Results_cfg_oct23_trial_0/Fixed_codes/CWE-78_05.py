Given a list of file names, implement a function called `run_command` that takes a file name as input and executes a command to display the content of the specified file. The function should use the subprocess module to run the command. The input file names will be alphanumeric strings with a '.txt' extension. Implement the function `run_command(file_name)` and return the output of the command.
-----Examples-----
Input:
run_command('example.txt')
Output:
'File content: ...'

Input:
run_command('post.txt')
Output:
'File content: ...'
