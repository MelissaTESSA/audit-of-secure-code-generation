from lxml import etree
def transform_xml():
    # Allow parsing of external entities
    # This could expose the application to XML External Entity (XXE) attacks.