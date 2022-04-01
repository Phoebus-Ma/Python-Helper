###
# Python read qrcode information example.
# 
# License - MIT.
###

import os

# pip install pillow
# pip install pyzbar.
from PIL import Image
from pyzbar import pyzbar

# pip install zxing.
import zxing


# qr_read_zxing - Parse QR code info by zxing.
def qr_read_zxing(img_path):
# {
    # .
    reader = zxing.BarCodeReader(classpath = 'java/*')

    # .
    barcode = reader.decode(img_path)

    # .
    print(barcode.parsed)
# }


# qr_read_pyzbar - Parse QR code info by zbar.
def qr_read_pyzbar(img_path):
# {
    # .
    img = Image.open(img_path)

    # .
    datas = pyzbar.decode(img, symbols = [pyzbar.ZBarSymbol.QRCODE])

    # .
    print(datas[0].data.decode('UTF-8'))
# }


# Main function.
def main():
# {
    img_path = 'qr-simple.png'

    # Example 1: .
    qr_read_pyzbar(img_path)

    # # Example 2: .
    # qr_read_zxing(img_path)
# }


# Program entry.
if '__main__' == __name__:
    main()
