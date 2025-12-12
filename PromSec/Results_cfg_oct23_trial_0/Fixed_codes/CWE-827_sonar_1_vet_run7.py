import os
import xml.etree.ElementTree as ET

xml_file_path = os.getenv('XML_FILE_PATH')

if xml_file_path:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    def print_element(element):
        print(f'Tag: {element.tag}')
        print(f'Attributes: {element.attrib}')
        print(f'Text: {element.text}')

        for child in element:
            print_element(child)

    print_element(root)
else:
    print('XML_FILE_PATH environment variable is not set.')