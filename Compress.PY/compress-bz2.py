###
# Python bzip2 compress/uncompress test.
# 
# License - MIT.
###

import os
import bz2


# bzip2_uncompress - Uncompress bzip2 file.
def bzip2_uncompress(islines):
# {
    with bz2.open(bzip2_name, 'rb') as fd_bz2:
        with open('bz2_' + file_name, 'wb') as fd:
            if (True == islines):
                fd.writelines(fd_bz2)
            else:
                fd.write(fd_bz2.read())
# }


# bzip2_compress - Compress bzip2 file.
def bzip2_compress(islines):
# {
    with bz2.open(bzip2_name, 'wb') as fd_bz2:
        with open(file_name, 'rb') as fd:
            if (True == islines):
                fd_bz2.writelines(fd)
            else:
                fd_bz2.write(fd.read())
# }


# Main function.
def main():
# {
    # Example 1: Compress bzip2 file.
    bzip2_compress(True)

    # Example 2: Uncompress bzip2 file.
    bzip2_uncompress(False)

    return 0
# }


# Program entry.
if '__main__' == __name__:
    bzip2_name      = 'README.md.bz2'
    file_name       = 'README.md'
    extract_path    = 'et_test'

    main()
