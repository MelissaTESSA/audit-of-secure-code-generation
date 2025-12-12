import os
import xml.etree.ElementTree as ET

xml_file_path = os.getenv('XML_FILE_PATH', 'Test/CWE-611_sonar_4/config.xml')

try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    for child in root:
        print(child.text)
except ET.ParseError as e:
    print(f"Error parsing XML file: {e}")
except FileNotFoundError:
    print("File not found.")