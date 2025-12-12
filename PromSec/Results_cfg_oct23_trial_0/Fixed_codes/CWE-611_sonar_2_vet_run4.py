import os
from lxml import etree

def get_root():
    parser = etree.XMLParser()
    tree = etree.parse(os.environ.get('CONFIG_FILE_PATH', 'Test/CWE-611_sonar_2/config.xsd'), parser)
    return tree.getroot()