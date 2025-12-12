import os
import xml.etree.ElementTree as ET

xml_file_path = os.getenv("XML_FILE_PATH")

if xml_file_path:
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        for elem in root.iter():
            print(f"Tag: {elem.tag}")
            print(f"Attributes: {elem.attrib}")
            print(f"Text: {elem.text}")

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("XML_FILE_PATH environment variable is not set.")