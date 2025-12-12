import os
import xml.etree.ElementTree as ET

try:
    secret_key = os.getenv('SECRET_KEY')
    tree = ET.parse('data.xml')
    root = tree.getroot()
    
    for elem in root.iter():
        print(elem.tag, elem.attrib)
        
except ET.ParseError:
    print('Error parsing XML file')
except Exception as e:
    print('An error occurred:', e)