import os

def readFile(fileName):
    if os.path.exists(fileName):
        try:
            with open(fileName, 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    else:
        print("File does not exist.")
        return None