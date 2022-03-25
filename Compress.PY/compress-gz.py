###
# Python gzip compress/uncompress test.
# 
# License - MIT.
###

import os
import gzip


# gzip_lines_uncompress - Uncompress gzip file.
def gzip_lines_uncompress(islines):
# {
    with gzip.open(gzip_name, 'rb') as fd_gz:
        with open('gz_' + file_name, 'wb') as fd:
            if (True == islines):
                fd.writelines(fd_gz)
            else:
                fd.write(fd_gz.read())
# }


# gzip_lines_compress - Compress gzip file.
def gzip_lines_compress(islines):
# {
    with gzip.open(gzip_name, 'wb') as fd_gz:
        with open(file_name, 'rb') as fd:
            if (True == islines):
                fd_gz.writelines(fd)
            else:
                fd_gz.write(fd.read())
# }


# Main function.
def main():
# {
    # Example 1: Compress gzip file.
    gzip_lines_compress(False)

    # Example 2: Uncompress gzip file.
    gzip_lines_uncompress(True)

    return 0
# }


# Program entry.
if '__main__' == __name__:
    gzip_name       = 'README.md.gz'
    file_name       = 'README.md'
    extract_path    = 'et_test'

    main()
