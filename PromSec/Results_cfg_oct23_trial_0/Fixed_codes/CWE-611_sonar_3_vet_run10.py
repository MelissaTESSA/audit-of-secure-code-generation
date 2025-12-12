import os
from lxml import etree

def transform_xml():
    parser = etree.XMLParser(remove_blank_text=True)
    file_path = os.path.join('Test', 'CWE-611_sonar_3', 'config.xsl')
    tree = etree.parse(file_path, parser)
    return etree.XSLT(tree)