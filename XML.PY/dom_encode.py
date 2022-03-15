####
# XML encode by DOM.
# 
# License - MIT. 
###

import os
from xml.dom.minidom import Document


'''
<?xml version="1.0" encoding="UTF-8"?>

<Market merchandise="Vegetable">

    <Vegetable title="Cucumber">
        <price>5</price>
        <counts>100</counts>
        <description>Green stick vegetables</description>
    </Vegetable>

    ...

</Market>
'''


# Main function.
def main():
# {
    # Test data.
    VegetableList = [
        {'title': 'Cucumber', 'price': 5,   'counts': 100, 'description': 'Green stick vegetable'},
        {'title': 'Tomato',   'price': 2.8, 'counts': 119, 'description': 'Red ball vegetable'},
        {'title': 'Potato',   'price': 2.2, 'counts': 178, 'description': 'Yellow oval vegetable'},
        {'title': 'Onion',    'price': 0.9, 'counts': 223, 'description': 'Purple ball vegetable'},
    ]

    # Create document.
    doc = Document()

    # Create root node.
    root_node = doc.createElement('Market')

    # Add root node attribute information.
    root_node.setAttribute('merchandise', 'Vegetable')

    # Add the root node to the newly created blank document.
    doc.appendChild(root_node)

    # Add child node and data to document.
    for mem in VegetableList:
        # Create a secondary node.
        vege_node = doc.createElement('Vegetable')
        vege_node.setAttribute('title', str(mem['title']))

        # Create a three level node.
        price_node  = doc.createElement('price')
        txt_node    = doc.createTextNode(str(mem['price']))
        price_node.appendChild(txt_node)

        # Create a three level node.
        counts_node = doc.createElement('counts')
        txt_node    = doc.createTextNode(str(mem['counts']))
        counts_node.appendChild(txt_node)

        # Create a three level node.
        desc_node   = doc.createElement('description')
        txt_node    = doc.createTextNode(str(mem['description']))
        desc_node.appendChild(txt_node)

        # Add a tier 3 node to a tier 2 node.
        vege_node.appendChild(price_node)
        vege_node.appendChild(counts_node)
        vege_node.appendChild(desc_node)

        # Add the data to root node.
        root_node.appendChild(vege_node)

    # Save XML data.
    f = open('vegetable.xml', 'w')

    doc.writexml(f, indent = '\t', addindent = '\t', newl = '\n', encoding = 'utf-8')

    f.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
