import tempfile

def write_results(results):
    """
    Write the results to a temporary file and return the path of the file.

    Args:
    results (str): The results to be written to the file.

    Returns:
    str: The path of the temporary file where the results were written.
    """
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(results)
        temp_file_path = temp_file.name
    return temp_file_path
