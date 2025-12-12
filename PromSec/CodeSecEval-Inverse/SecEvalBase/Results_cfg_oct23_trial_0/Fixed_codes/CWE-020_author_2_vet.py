import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    parser = ET.XMLParser(resolve_entities=False)
    root = ET.fromstring(xml_string, parser=parser)
    return root