import os
import xml.etree.ElementTree as ET

xml_file_path = os.getenv('XML_FILE_PATH')

if xml_file_path:
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        for child in root:
            print(child.tag)
            print(child.attrib)
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except FileNotFoundError:
        print("File not found")
else:
    print("Environment variable XML_FILE_PATH is not set")