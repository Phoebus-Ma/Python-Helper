####
# XML encode by SAX.
# 
# License - MIT. 
###

import os
import sys
from xml.sax.saxutils import XMLGenerator


# Class for write vegetable xml.
class VegetableWriter():
# {
    # Initialize.
    def __init__(self, output, encoding):
    # {
        vege_writer = XMLGenerator(output, encoding)

        vege_writer.startDocument()
        vege_writer.startElement('Market', {'merchandise': 'Vegetables'})

        self._writer    = vege_writer
        self._output    = output
        self._encoding  = encoding
    # }


    # Class close.
    def close(self):
    # {
        self._writer.endElement('Market')
        self._writer.endDocument()
    # }


    # Write XML data.
    def write(self):
    # {
        self._writer.startElement('Vegetable', {'title': 'Potato'})

        self._writer.startElement('price', {})
        self._writer.characters('2.2')
        self._writer.endElement('price')

        self._writer.startElement('counts', {})
        self._writer.characters('178')
        self._writer.endElement('counts')

        self._writer.startElement('description', {})
        self._writer.characters('Yellow oval vegetable')
        self._writer.endElement('description')

        self._writer.endElement('Vegetable')
    # }
# }


# Main function.
def main():
# {
    vege_creator = VegetableWriter(sys.stdout, 'utf-8')
    vege_creator.write()
    vege_creator.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
