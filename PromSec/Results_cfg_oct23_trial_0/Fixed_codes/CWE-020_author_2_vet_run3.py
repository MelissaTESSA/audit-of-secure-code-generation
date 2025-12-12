import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)
        return root
    except ET.ParseError:
        print("Error parsing XML")
        return None

xml_string = "<data><name>John Doe</name><age>30</age></data>"
parsed_xml = parse_xml(xml_string)

if parsed_xml is not None:
    print(parsed_xml.tag)