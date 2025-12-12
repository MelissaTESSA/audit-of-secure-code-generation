import os

def process_input_file(filename):
    if not os.path.exists(filename):
        return "Invalid filename."
    
    os.system(f'cat {filename}')
    
    return "Data from the file has been processed."