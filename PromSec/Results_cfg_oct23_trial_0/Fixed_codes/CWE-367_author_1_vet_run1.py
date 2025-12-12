import os

def readFile(fileName):
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            content = file.read()
        return content
    else:
        return None