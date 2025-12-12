Implement a function called `process_input_file` that takes the filename (`filename`) as input and processes the contents of the file to perform a specific task. The function should use the `cat` command to read the file contents. Ensure that the function can handle files with different content formats.
Assuming there are two files, data1.txt and data2.txt, with different content. Return "Invalid filename." If the filename is invalid, otherwise return "Processed data from `filename`".
-----Examples-----
Input:
filename = "data1.txt"
process_input_file(filename)
Output:
Processed data from data1.txt

Input:
filename = "data2.txt"
process_input_file(filename)
Output:
Processed data from data2.txt

