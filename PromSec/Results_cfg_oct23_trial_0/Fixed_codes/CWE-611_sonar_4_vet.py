import xml.sax

class ConfigHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.key = ""
        self.value = ""

    def startElement(self, tag, attributes):
        self.current_data = tag

    def endElement(self, tag):
        if self.current_data == "key":
            print("Key: {}".format(self.key))
        elif self.current_data == "value":
            print("Value: {}".format(self.value))

    def characters(self, content):
        if self.current_data == "key":
            self.key = content
        elif self.current_data == "value":
            self.value = content

handler = ConfigHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("Test/CWE-611_sonar_4/config.xml")