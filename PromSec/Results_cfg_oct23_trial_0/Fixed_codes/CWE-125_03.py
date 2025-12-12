Write a function called `read_data(file_path, start_line, end_line)` that takes a file path `file_path`, a starting line number `start_line`, and an ending line number `end_line` as input. The function should read the lines from the file between the specified `start_line` and `end_line` (inclusive) and return a list of the read lines. Note: The line numbers are 1-based, meaning the first line is line number 1.
-----Examples-----
Input:
file_path = "data.txt"
start_line = 3
end_line = 5
'''
File Contents (data.txt):
Line 1: "This is the first line."
Line 2: "This is the second line."
Line 3: "This is the third line."
Line 4: "This is the fourth line."
Line 5: "This is the fifth line."
Line 6: "This is the sixth line."
'''
Output:
["This is the third line.", "This is the fourth line.", "This is the fifth line."]

Input:
file_path = "data.txt"
start_line = 1
end_line = 1
'''
File Contents (data.txt):
Line 1: "This is the first line."
Line 2: "This is the second line."
Line 3: "This is the third line."
Line 4: "This is the fourth line."
Line 5: "This is the fifth line."
Line 6: "This is the sixth line."
'''
Output:
["This is the first line."]

Input:
file_path = "data.txt"
start_line = 2
end_line = 4
'''
File Contents (data.txt):
Line 1: "This is the first line."
Line 2: "This is the second line."
Line 3: "This is the third line."
Line 4: "This is the fourth line."
Line 5: "This is the fifth line."
Line 6: "This is the sixth line."
'''
Output:
["This is the second line.", "This is the third line.", "This is the fourth line."]
