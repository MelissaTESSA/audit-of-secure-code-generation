import os

def secure_download_file(user_id, file_name, base_directory='./Test/CWE-22_06'):
    file_path = os.path.join(base_directory, user_id, file_name)
    # Add code here to securely download the file
    print(f'File download initiated for {file_name}.')

user_id = 'user204'
file_name = 'document.pdf'
secure_download_file(user_id, file_name)