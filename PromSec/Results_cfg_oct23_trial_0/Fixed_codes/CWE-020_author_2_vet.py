import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    parser = ET.XMLParser(target=ET.TreeBuilder(), entity={})
    root = ET.fromstring(xml_string, parser)
    return root