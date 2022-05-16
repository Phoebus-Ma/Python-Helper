###
# MD5 encryption example.
# 
# License - MIT.
####

import os
import hashlib


# Main function.
def main():
# {
    teststr = 'To be No.1'

    hmd5 = hashlib.md5()
    hmd5.update(teststr.encode(encoding = 'UTF-8'))

    print('Source data:\t' + teststr)
    print('Dest data:\t' + hmd5.hexdigest())
# }


# Program entry.
if '__main__' == __name__:
    main()
