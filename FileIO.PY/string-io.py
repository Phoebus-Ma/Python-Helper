###
# Common memory data read and write example.
# 
# License - MIT.
###

import os
from io import StringIO


# Read/write data in memory, style 2.
def operating_data2(buffer):
# {
    with StringIO(buffer) as f:
        while True:
            rstr = f.readline()

            if ('' == rstr):
                break

            print(rstr)
# }


# Read/write data in memory, style 1.
def  operating_data1(buffer):
# {
    with StringIO() as f:
        f.write(buffer)

        print(f.getvalue())
# }


# Main function.
def main():
# {
    test_str = 'The sky is unlimited for birds to fly at ease.'

    operating_data1(test_str)

    operating_data2(test_str)
# }


# Program entry.
if '__main__' == __name__:
    main()
