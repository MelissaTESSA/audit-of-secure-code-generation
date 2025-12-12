import os
import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    for child in root:
        print(child.tag, child.text)

if __name__ == "__main__":
    xml_data = input("Enter XML data: ")
    parse_xml(xml_data)