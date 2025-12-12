import tempfile

def write_results(results):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(results)
        temp_file_path = temp_file.name
    return f'Results written to {temp_file_path}'