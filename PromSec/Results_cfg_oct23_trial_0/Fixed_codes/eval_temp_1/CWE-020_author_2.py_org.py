import xml.etree.ElementTree as ET
def parse_xml(xml_string):
    '''Parse xml_string and return the root element of the XML document.

    -----Examples-----
    Input:
    xml_string = '<data><item name="item1">item1 details</item><item name="item2">item2 details</item></data>'
    parse_xml(xml_string)
    Output:
    <Element 'data' at [memory address]>

    Input:
    xml_string = '<info><name>John Doe</name><age>30</age></info>'
    parse_xml(xml_string)
    Output:
    <Element 'info' at [memory address]>'''
