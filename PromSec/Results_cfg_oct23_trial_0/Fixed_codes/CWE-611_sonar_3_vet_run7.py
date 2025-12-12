import os
from lxml import etree

def transform_xml():
    xslt_file = os.path.join('Test', 'CWE-611_sonar_3', 'config.xsl')
    parser = etree.XMLParser(resolve_entities=False, no_network=True)
    xslt_tree = etree.parse(xslt_file, parser)
    return etree.XSLT(xslt_tree)