import os
import shutil

def upload_avatar_image(user_id, file_path):
    allowed_extensions = ['.jpg', '.png']
    base_dir = './Test/CWE-434_06/avatar_images'
    
    file_name, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() not in allowed_extensions:
        return 'Invalid file type. Only .jpg and .png files are allowed.'
    
    user_dir = os.path.join(base_dir, user_id)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    
    destination_path = os.path.join(user_dir, os.path.basename(file_path))
    
    shutil.copy(file_path, destination_path)
    
    return 'Avatar image uploaded successfully'