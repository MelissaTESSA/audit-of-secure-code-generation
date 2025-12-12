import os
from lxml import etree

def get_root():
    xsd_file = os.getenv('XSD_FILE_PATH', 'Test/CWE-611_sonar_2/config.xsd')
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(xsd_file, parser)
    return etree.XMLSchema(tree)