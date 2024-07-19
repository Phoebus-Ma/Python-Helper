####
# XML decode by DOM.
# 
# License - MIT. 
###

import os
from xml.dom.minidom import parse


# Main function.
def main():
# {
    # Create XML data tree by dom.
    data_tree = parse('fruits.xml')

    # Get document element.
    market = data_tree.documentElement

    # Display root node attribute information.
    if market.hasAttribute('merchandise'):
        merchandise = market.getAttribute('merchandise')
        print('--------%s--------' % merchandise)

    # Get all content data.
    fruits = market.getElementsByTagName('Fruit')

    # Parse content data.
    for fruit in fruits:
        # Secondary node data.
        # Title.
        title = fruit.getAttribute('title')
        print('----------------')
        print('title: %s' % title)

        # Three-level node data.
        # Price.
        price = fruit.getElementsByTagName('price')[0]
        print('price: %s' % price.childNodes[0].data)

        # Counts.
        counts = fruit.getElementsByTagName('counts')[0]
        print('counts: %s' % counts.childNodes[0].data)

        # Description.
        description = fruit.getElementsByTagName('description')[0]
        print('description: %s' % description.childNodes[0].data)
# }


# Program entry.
if '__main__' == __name__:
    main()
