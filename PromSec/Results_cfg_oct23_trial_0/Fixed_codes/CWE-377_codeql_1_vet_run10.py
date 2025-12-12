import os
import tempfile

def write_results(results):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    with open(temp_file.name, 'w') as file:
        file.write(results)
    return f'Results written to {temp_file.name}'