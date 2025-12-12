import subprocess

def search_files(search_term, file_name):
    try:
        result = subprocess.run(["grep", search_term, file_name], capture_output=True, text=True, check=True)
        if result.returncode == 0:
            return result.stdout.splitlines()
        else:
            return []
    except subprocess.CalledProcessError:
        return []
    except Exception:
        return []

print(search_files("hello", "example.txt"))
print(search_files("world", "example.txt"))