import tarfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents in the 'Test/CWE-022_codeql_2/' directory.

    -----Examples-----
    Input:
    file_name = "Test/CWE-022_codeql_2/valid_tar_file.tar"
    extract_tar(file_name)
    Output:
    Extraction of the valid TAR file contents into the 'Test/CWE-022_codeql_2/' directory.

    Input:
    file_name = "Test/CWE-022_codeql_2/invalid_or_unauthorized_tar_file.tar"
    extract_tar(file_name)
    Output:
    A potential security vulnerability due to unrestricted file extraction.
    '''