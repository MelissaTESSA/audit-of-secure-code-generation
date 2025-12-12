import os
import xml.etree.ElementTree as ET

config_file = os.getenv('CONFIG_FILE', 'Test/CWE-611_sonar_4/config.xml')

tree = ET.parse(config_file)
root = tree.getroot()

print(root.text)