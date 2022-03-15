####
# XML decode by SAX.
# 
# License - MIT. 
###

import os
import xml.sax


# Class for fruits xml parse.
class FruitsHandler(xml.sax.ContentHandler):
# {
    # Initialize.
    def __init__(self):
    # {
        self.tmpdata        = ''
        self.price          = ''
        self.counts         = ''
        self.description    = ''
    # }


    # The element starts the event handler.
    def startElement(self, tag, attributes):
    # {
        self.tmpdata = tag

        if 'fruits' == tag:
            title = attributes['title']

            print('-------------------------')
            print('Title: %s' % title)
    # }


    # The element ends the event handler.
    def endElement(self, tag):
    # {
        if 'price' == self.tmpdata:
            print('price: %s' % self.price)
        elif 'counts' == self.tmpdata:
            print('counts: %s' % self.counts)
        elif 'description' == self.tmpdata:
            print('description: %s.' % self.description)

        self.tmpdata = ''
    # }


    # Element content event handler.
    def characters(self, content):
    # {
        if 'price' == self.tmpdata:
            self.price = content
        elif 'counts' == self.tmpdata:
            self.counts = content
        elif 'description' == self.tmpdata:
            self.description = content
    # }
# }


# Main function.
def main():
# {
    # Create SAX parser.
    parser = xml.sax.make_parser()

    # Turn off namespace.
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # Rewrite content handler.
    fruitsHandler = FruitsHandler()
    parser.setContentHandler(fruitsHandler)

    # Start parse.
    parser.parse('fruits.xml')
# }


# Program entry.
if '__main__' == __name__:
    main()

