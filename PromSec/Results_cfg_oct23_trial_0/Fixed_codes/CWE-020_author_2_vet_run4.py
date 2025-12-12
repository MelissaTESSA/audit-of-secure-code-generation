import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    for child in root:
        print(child.tag, child.text)

parse_xml("<data><name>John Doe</name><age>25</age></data>")