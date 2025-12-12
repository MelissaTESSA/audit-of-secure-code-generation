import os

def execute_code(code, language):
    directory = 'Test/CWE-276_02'
    os.makedirs(directory, exist_ok=True)
    
    file_name = os.path.join(directory, 'script.py')
    
    with open(file_name, 'w') as file:
        file.write(code)
    
    os.chmod(file_name, 0o500)

# Example usage:
# execute_code("print('Hello, World!')", 'python')