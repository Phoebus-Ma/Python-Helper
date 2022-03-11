###
# Read file example.
# 
# License - MIT.
###

import os


# Main function.
def main():
# {
    f = open('testfile.txt', 'a')

    f.write('\nTo be no.1.')

    f.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
