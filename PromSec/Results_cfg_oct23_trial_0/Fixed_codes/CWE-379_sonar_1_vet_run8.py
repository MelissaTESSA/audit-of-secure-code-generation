import tempfile

def write_results(results):
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write(results)
        return temp_file.name