import os
from lxml import etree

def getXmlRoot():
    xml_file_path = os.path.join('Test', 'CWE-827_sonar_1', 'c.xml')
    parser = etree.XMLParser(resolve_entities=False)
    tree = etree.parse(xml_file_path, parser)
    root = tree.getroot()
    return root