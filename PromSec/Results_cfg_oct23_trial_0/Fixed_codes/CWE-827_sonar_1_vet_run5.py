import os
import xml.etree.ElementTree as ET

try:
    secret_key = os.environ.get('SECRET_KEY')
    if secret_key is None:
        raise ValueError('Secret key not found')

    tree = ET.parse('data.xml')
    root = tree.getroot()

    for elem in root.iter():
        print(elem.tag, elem.attrib)

except ValueError as e:
    print(e)

except ET.ParseError as e:
    print('Parsing error in XML file', e)

except Exception as e:
    print('An error occurred', e)