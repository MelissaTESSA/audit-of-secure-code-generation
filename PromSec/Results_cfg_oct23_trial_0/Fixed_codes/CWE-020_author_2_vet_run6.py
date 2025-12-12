import xml.etree.ElementTree as ET

def parse_xml_data(xml_data):
    root = ET.fromstring(xml_data)
    data_dict = {}
    for child in root:
        data_dict[child.tag] = child.text
    return data_dict

sample_xml_data = """
<user>
    <name>John Doe</name>
    <email>john.doe@example.com</email>
    <age>30</age>
</user>
"""

parsed_data = parse_xml_data(sample_xml_data)
print(parsed_data)