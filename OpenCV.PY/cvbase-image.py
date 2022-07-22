###
# Python opencv operate image example.
# 
# License - MIT.
###

import os

# pip install opencv-python
import cv2 as cv
import numpy


# edit_image - Base edit image.
def edit_image(file_path):
# {
    color_img   = cv.imread(file_path)

    # Splite RGB image.
    baseclr     = cv.split(color_img)

    cv.imshow('color1', color_img)
    cv.imshow('blue',   baseclr[0])
    cv.imshow('green',  baseclr[1])
    cv.imshow('red',    baseclr[2])

    # Resize image.
    re_img      = cv.resize(color_img, (320, 320))

    cv.imshow('resize', re_img)

    # Increase the dimension: HWC(high, width, channel) to NCHW.
    print(re_img.shape)

    nchw_img = re_img.transpose(2, 0, 1)        # H(0), W(1), C(2) to CHW.
    print(nchw_img.shape)

    ## expand_dims is add, squeeze is del.
    nchw_img = numpy.expand_dims(nchw_img, 0)   # CHW add N.
    print(nchw_img.shape)

    # Traverse the pixel.
    h, w, c = re_img.shape

    for row in range(h):
        for col in range(w):
            b, g, r = re_img[row, col]
            print(b, g, r)

    cv.waitKey(0)
    cv.destroyAllWindows()
# }


# show_image - Base display image.
def show_image(file_path):
# {
    color_img   = cv.imread(file_path)
    gray_img    = cv.cvtColor(color_img, cv.COLOR_BGR2GRAY)

    cv.imshow('color', color_img)
    cv.imshow('gray',  gray_img)

    cv.waitKey(0)
    cv.destroyAllWindows()
# }


# Main function.
def main():
# {
    show_image(img_path)
    edit_image(img_path)
# }


# Program entry.
if '__main__' == __name__:
# {
    # Replace your image path.
    img_path = 'D:/banana.jpeg'

    main()
# }
