import os
from lxml import etree

def get_root():
    file_path = 'Test/CWE-611_sonar_1/config.xml'
    
    if os.path.exists(file_path):
        parser = etree.XMLParser(resolve_entities=False, remove_blank_text=True)
        tree = etree.parse(file_path, parser)
        root = tree.getroot()
        return root

    return None