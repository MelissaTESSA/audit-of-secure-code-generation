import os
import xml.etree.ElementTree as ET

secret_key = os.getenv('SECRET_KEY')

if secret_key is None:
    print("Secret key not available")
else:
    try:
        tree = ET.parse('data.xml')
        root = tree.getroot()
        
        for elem in root.iter():
            print(elem.tag, elem.attrib)
    
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")