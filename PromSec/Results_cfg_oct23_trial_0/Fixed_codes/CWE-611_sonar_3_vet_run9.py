import os
from lxml import etree

def transform_xml():
    file_path = os.getenv('XML_FILE_PATH', 'Test/CWE-611_sonar_3/config.xsl')
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    tree = etree.parse(file_path, parser)
    return etree.XSLT(tree)