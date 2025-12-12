import os
import xml.etree.ElementTree as ET

try:
    xml_file_path = os.getenv('XML_FILE_PATH', 'Test/CWE-611_sonar_4/config.xml')
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    print(root.text)
except Exception as e:
    print(f"An error occurred: {e}")