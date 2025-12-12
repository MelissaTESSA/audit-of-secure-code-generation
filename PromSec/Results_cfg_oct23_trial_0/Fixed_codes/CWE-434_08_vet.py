import os

def upload_web_template(user_id, file_name, file_content, file_type, base_dir):
    if file_type not in ['html', 'css']:
        return 'Invalid file type. Only html and css files are allowed.'
    
    file_path = os.path.join(base_dir, file_name)
    
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    return 'Web template uploaded successfully'