###
# Python create qrcode picture example.
# 
# License - MIT.
###

import os

# pip install qrcode.
# pip install pillow.
import qrcode


# qr_write_by_args - Create QR code by parameters.
def qr_write_by_args(data):
# {
    # Version: 1~40, v1: 21x21, v2: 25x25, v3: 29x29..., v40: 177x177.
    qr = qrcode.QRCode(
        version             = 7,
        error_correction    = qrcode.constants.ERROR_CORRECT_H,
        box_size            = 10,
        border              = 4
    )

    # Add need create qr data.
    qr.add_data(data)

    # Compile the data into a QR Code array.
    qr.make(fit = True)

    # Create qr code image.
    img = qr.make_image()

    # Save image.
    img.save('qr-args.png')
# }


# qr_write_info - Create QR code by data.
def qr_write_simple(data):
# {
    img = qrcode.make(data)
    img.save('qr-simple.png')
# }


# Main function.
def main():
# {
    data = 'https://www.kernel.org/'

    # Example 1: Create simple qrcode picture.
    print('-----------Example 1-----------')
    qr_write_simple(data)
    print('Done 1.')

    # Example 2: Create qrcode by parameters.
    print('-----------Example 1-----------')
    qr_write_by_args(data)
    print('Done 2.')
# }


# Program entry.
if '__main__' == __name__:
    main()
