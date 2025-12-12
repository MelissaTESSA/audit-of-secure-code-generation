import os
from lxml import etree

def get_root():
    file_path = os.path.join('Test', 'CWE-611_sonar_1', 'config.xml')
    
    parser = etree.XMLParser(resolve_entities=False)
    tree = etree.parse(file_path, parser)
    root = tree.getroot()
    
    return root