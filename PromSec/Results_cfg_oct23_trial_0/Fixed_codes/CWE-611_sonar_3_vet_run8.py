import os
from lxml import etree

def transform_xml():
    parser = etree.XMLParser(remove_blank_text=True)
    xslt_file = os.path.join('Test', 'CWE-611_sonar_3', 'config.xsl')
    xslt = etree.parse(xslt_file, parser)
    return etree.XSLT(xslt)