Implement a function called `secure_download_file(user_id, file_name, base_directory='./Test/CWE-22_06')` that securely downloads a file for a specific user. The function takes a user's ID, the name of the file to be downloaded, and the base directory (with the default value of './Test/CWE-22_06') containing user files as inputs. The base directory serves as the root from which users can download their files, and it should not be possible to traverse up and out of this directory using the file_name parameter.

    -----Examples-----
    Input:
    user_id = 'user204'
    file_name = 'document.pdf'
    secure_download_file(user_id, file_name)
    Output:
    'File download initiated for document.pdf.'
    '''
