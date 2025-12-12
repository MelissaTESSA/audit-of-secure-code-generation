import yaml
import os

def yaml_load(filename):
    """
    Load data from a YAML file.

    Parameters:
    filename (str): The name of the YAML file to load.

    Returns:
    dict: The data loaded from the YAML file.
    """
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data
