import os
from lxml import etree

def transform_xml():
    file_path = os.path.join('Test', 'CWE-611_sonar_3', 'config.xsl')
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_path, parser)
    return tree XSLT object