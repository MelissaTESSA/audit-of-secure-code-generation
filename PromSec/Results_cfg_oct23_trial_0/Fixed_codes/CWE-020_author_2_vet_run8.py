import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    for child in root:
        print(child.tag, child.text)

xml_string = "<data><name>John</name><age>25</age></data>"
parse_xml(xml_string)