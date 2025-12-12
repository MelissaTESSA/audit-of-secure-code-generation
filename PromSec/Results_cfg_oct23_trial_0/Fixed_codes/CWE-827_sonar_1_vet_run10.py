import os
import xml.etree.ElementTree as ET

try:
    xml_file_path = os.getenv('XML_FILE_PATH')
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    for child in root:
        print(child.tag, child.attrib)
        
except Exception as e:
    print(f"An error occurred: {e}")