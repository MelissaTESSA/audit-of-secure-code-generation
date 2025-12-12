import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)
        return root
    except ET.ParseError:
        print("Error parsing XML")
        return None

xml_string = "<data><item>Item 1</item><item>Item 2</item></data>"
root = parse_xml(xml_string)

if root is not None:
    print(root.tag)