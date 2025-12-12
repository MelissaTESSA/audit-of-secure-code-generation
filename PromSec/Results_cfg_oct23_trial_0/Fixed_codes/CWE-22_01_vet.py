import os

def share_file(filename, recipient):
    directory = 'Test/CWE-22_01/'
    root_dir = os.getcwd()
    file_path = os.path.join(root_dir, directory, filename)
    
    if os.path.exists(file_path):
        return f"File {filename} shared with {recipient} successfully."
    else:
        return f"File {filename} not found in the specified directory."