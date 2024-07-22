###
# Single picture conversion example.
# 
# License - MIT.
###

import os
# pip install pillow
from PIL import Image


# Main function.
def main():
# {
    image = Image.open(original_pic)
    image.save(result_pic)
# }


# Program entry.
if '__main__' == __name__:

    # Replace it with an actual image.
    original_pic = 'potato1.jpg'
    result_pic   = 'potato1.png'

    main()
