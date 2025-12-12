import os
import xml.etree.ElementTree as ET

def read_xml_content(file_path):
    content_list = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for element in root.iter():
            if element.text:
                content_list.append(element.text)
    except ET.ParseError:
        print("Error parsing XML file.")
    
    return content_list

if 'XML_FILE_PATH' in os.environ:
    file_path = os.environ['XML_FILE_PATH']
    if os.path.exists(file_path):
        content_list = read_xml_content(file_path)
        if content_list:
            for content in content_list:
                print(content)
        else:
            print("No text content found in the XML file.")
    else:
        print("Invalid file path.")
else:
    print("XML_FILE_PATH environment variable is not set.")