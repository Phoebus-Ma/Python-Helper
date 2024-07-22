###
# Multi picture conversion example.
# 
# License - MIT.
###

import os
# pip install opencv-python
import cv2


# Main function.
def main():
# {
    i = 0

    for x in os.listdir(path):
    # {
        # Read original picture.
        image = cv2.imread(r'{}\{}'.format(path, x))

        # Conversion pic format to PNG.
        cv2.imwrite(r'{}\{}.png'.format(path, i), image)

        i += 1
    # }
# }


# Program entry.
if '__main__' == __name__:

    # Replace a real folder.
    path = r'potatos'

    main()
