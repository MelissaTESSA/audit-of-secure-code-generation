import os
import xml.etree.ElementTree as ET

xml_file_path = os.getenv('XML_FILE_PATH')

tree = ET.parse(xml_file_path)
root = tree.getroot()

print(root.tag)