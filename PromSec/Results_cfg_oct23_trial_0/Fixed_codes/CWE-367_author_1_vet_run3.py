import os

def readFile(fileName):
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            content = file.read()
        return content

# Example usage
# content = readFile('example.txt')
# if content:
#     print(content)