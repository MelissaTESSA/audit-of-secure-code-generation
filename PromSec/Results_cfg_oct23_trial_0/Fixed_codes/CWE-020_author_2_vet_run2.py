import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)
        return root
    except ET.ParseError:
        print("Error parsing XML")
        return None

xml_string = "<items><item>Apple</item><item>Orange</item><item>Banana</item></items>"

root = parse_xml(xml_string)

if root is not None:
    for item in root.findall('item'):
        print(item.tag, item.text)