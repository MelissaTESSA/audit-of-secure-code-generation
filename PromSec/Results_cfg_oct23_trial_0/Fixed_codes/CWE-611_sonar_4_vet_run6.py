import os
import xml.etree.ElementTree as ET

try:
    tree = ET.parse('Test/CWE-611_sonar_4/config.xml')
except FileNotFoundError:
    raise FileNotFoundError("File not found")
except ET.ParseError:
    print("Error parsing XML file")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")