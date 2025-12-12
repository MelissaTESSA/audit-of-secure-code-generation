import os

def read_data(file_path, start_line, end_line):
    result = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(start_line-1, end_line):
            result.append(lines[i].strip())
    return result