import os

def rename_file(old_name, new_name):
    try:
        os.system(f"mv {old_name} {new_name}")
        return 'File renamed successfully'
    except Exception as e:
        return f'Error renaming file: {str(e)}'