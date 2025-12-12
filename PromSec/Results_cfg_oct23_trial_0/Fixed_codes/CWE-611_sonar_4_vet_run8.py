import xml.etree.ElementTree as ET

def read_xml_attribute(file_path, attribute_name):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root.get(attribute_name)
    except Exception as e:
        print(f"Error: {e}")
        return None

print(read_xml_attribute('Test/CWE-611_sonar_4/config.xml', 'root'))