def readFile(fileName):
    import os
    
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            content = file.read()
        return content