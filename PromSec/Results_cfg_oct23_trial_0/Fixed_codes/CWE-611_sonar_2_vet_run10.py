import os
from lxml import etree

def get_root():
    xsd_file = os.path.join('Test', 'CWE-611_sonar_2', 'config.xsd')
    parser = etree.XMLParser()
    tree = etree.parse(xsd_file, parser)
    return etree.XMLSchema(tree)