import os
import xml.etree.ElementTree as ET

def read_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    for elem in root.iter():
        print(f"Tag: {elem.tag}")
        print(f"Attributes: {elem.attrib}")
        print(f"Text: {elem.text}")

if 'XML_FILE_PATH' in os.environ:
    xml_file_path = os.environ['XML_FILE_PATH']
    read_xml_file(xml_file_path)
else:
    print("The 'XML_FILE_PATH' environment variable is not set.")