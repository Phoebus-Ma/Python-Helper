###
# Binary memory data read and write example.
# 
# License - MIT.
###

import os
from io import BytesIO


# Main function.
def main():
# {
    buffer = 'Happy.'

    with BytesIO() as f:
        f.write(buffer.encode('utf-8'))

        print(f.getvalue())
# }


# Program entry.
if '__main__' == __name__:
    main()
