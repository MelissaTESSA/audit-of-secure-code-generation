import os
import subprocess

def execute_code_snippet(language, code_snippet):
    if language != "python":
        return "Unsupported language"
    
    try:
        with open("temp_code.py", "w") as file:
            file.write(code_snippet)
        
        process = subprocess.Popen(["python", "temp_code.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            return stderr.decode()
        
        return stdout.decode()
    
    except Exception as e:
        return str(e)
    
    finally:
        if os.path.exists("temp_code.py"):
            os.remove("temp_code.py")