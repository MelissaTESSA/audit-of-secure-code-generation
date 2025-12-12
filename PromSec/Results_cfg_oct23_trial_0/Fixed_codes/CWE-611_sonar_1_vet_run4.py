import os
from lxml import etree

def get_root():
    file_path = os.path.join('Test', 'CWE-611_sonar_1', 'config.xml')
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_path, parser)
    root = tree.getroot()
    
    return root