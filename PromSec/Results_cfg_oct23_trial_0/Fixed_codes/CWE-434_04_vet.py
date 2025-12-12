import os

def txtxml_upload_file(file_content, file_name, directory):
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    return f"File {file_name} uploaded successfully to {directory}"