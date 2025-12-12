import os
import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print(name)

def main():
    xml_file_path = os.getenv('XML_FILE_PATH', 'Test/CWE-611_sonar_4/config.xml')
    handler = MyHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file_path)

if __name__ == "__main__":
    main()