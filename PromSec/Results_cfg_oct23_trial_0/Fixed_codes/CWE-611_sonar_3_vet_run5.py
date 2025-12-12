import os
from lxml import etree

def transform_xml():
    xslt_file = os.getenv('XSLT_FILE_PATH', 'Test/CWE-611_sonar_3/config.xsl')
    parser = etree.XMLParser(resolve_entities=False)
    xslt_tree = etree.parse(xslt_file, parser)
    return etree.XSLT(xslt_tree)