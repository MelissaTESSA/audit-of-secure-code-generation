import os
import xml.etree.ElementTree as ET

xml_file = os.getenv("XML_FILE")

if xml_file:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    for child in root:
        print(child.tag, child.text)
else:
    print("XML_FILE environment variable not set")