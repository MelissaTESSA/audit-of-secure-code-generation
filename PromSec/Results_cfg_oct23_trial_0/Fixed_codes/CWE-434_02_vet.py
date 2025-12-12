import os

def file_upload(file, upload_path):
    allowed_extensions = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
    if file.filename.split('.')[-1] in allowed_extensions:
        file.save(os.path.join(upload_path, file.filename))
        return "File securely uploaded."
    else:
        return "File type not allowed for upload."