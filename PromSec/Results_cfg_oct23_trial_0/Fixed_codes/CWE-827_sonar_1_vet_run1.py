import os
import xml.etree.ElementTree as ET

xml_file_path = os.getenv('XML_FILE_PATH')

if xml_file_path:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    for child in root:
        print(child.tag)
        print(child.attrib)