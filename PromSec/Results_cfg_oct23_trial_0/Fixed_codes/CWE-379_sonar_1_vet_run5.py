import tempfile

def write_results(results):
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write(results)
        temp_file_path = temp_file.name
    return temp_file_path