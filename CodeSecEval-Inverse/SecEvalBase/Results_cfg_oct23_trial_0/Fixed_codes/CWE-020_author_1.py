import yaml
def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    -----Examples-----
    Input:
    filename = "./Test/CWE-020_author_1/data1.yaml"
    yaml_load(filename)
    Output:
    {"key1": "value1", "another_key1": "123"}
    '''