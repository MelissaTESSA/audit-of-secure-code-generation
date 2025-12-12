import tempfile

def write_results_to_temp_file(results):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(results)
        temp_file_path = temp_file.name
    return temp_file_path