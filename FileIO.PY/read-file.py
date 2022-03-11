###
# Read file example.
# 
# License - MIT.
###

import os


# Main function.
def main():
# {
    f = open('testfile.txt', 'r')

    # Read style 1.
    print(f.read(5))
    print('--------------')

    # Read style 2.
    f.seek(0)
    for i in range(5):
        print(f.readline())
    print('--------------')

    # Read style 3.
    f.seek(0)
    print(f.read())
    print('--------------')

    # Read style 4.
    f.seek(0)
    for c in f:
        print(c)

    f.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
