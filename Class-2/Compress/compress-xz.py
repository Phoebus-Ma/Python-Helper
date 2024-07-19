###
# Python xz compress/uncompress test.
# 
# License - MIT.
###

import os
import lzma


# xz_uncompress - Uncompress xz file.
def xz_uncompress(islines):
# {
    with lzma.open(xzip_name, 'rb') as fd_xz:
        with open('xz_' + file_name, 'wb') as fd:
            if (True == islines):
                fd.writelines(fd_xz)
            else:
                fd.write(fd_xz.read())
# }


# xz_compress - Compress xz file.
def xz_compress(islines):
# {
    with lzma.open(xzip_name, 'wb') as fd_xz:
        with open(file_name, 'rb') as fd:
            if (True == islines):
                fd_xz.writelines(fd)
            else:
                fd_xz.write(fd.read())
# }


# Main function.
def main():
# {
    # Example 1: Compress xz file.
    xz_compress(False)

    # Example 2: Uncompress xz file.
    xz_uncompress(True)

    return 0
# }


# Program entry.
if '__main__' == __name__:
    xzip_name       = 'README.md.xz'
    file_name       = 'README.md'
    extract_path    = 'et_test'

    main()
