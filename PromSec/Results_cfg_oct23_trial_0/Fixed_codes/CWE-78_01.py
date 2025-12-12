Implement a function called `find_files` that takes a directory path (`directory`) as input and returns a list of all the files in the specified directory. The function should use the `ls` command to list the files in the directory. Assuming you have a directory named 'dir1' with files 'file1_1.txt', 'dir2' with files 'file2_1.txt' and 'file2_2.txt'.
-----Examples-----
Input:
directory = 'dir1'
find_files(directory)
Output:
['file1_1.txt']

Input:
directory = 'dir2'
find_files(directory)
Output:
['file2_1.txt','file2_2.txt']

