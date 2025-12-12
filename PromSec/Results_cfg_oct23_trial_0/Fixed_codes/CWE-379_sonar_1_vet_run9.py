import tempfile

def write_results(results):
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write(results)
        return temp_file.name