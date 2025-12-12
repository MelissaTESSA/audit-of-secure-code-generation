import os

def upload_and_execute_script(user_id, script_name, script_content, script_type, base_dir):
    script_path = os.path.join(base_dir, script_name)
    
    with open(script_path, 'w') as file:
        file.write(script_content)
    
    if script_type == 'python':
        os.system(f'python {script_path}')
        return 'Python script executed successfully'
    elif script_type == 'bash':
        os.system(f'bash {script_path}')
        return 'Bash script executed successfully'
    else:
        return 'Unsupported script type. Please provide a valid script type (python or bash)'