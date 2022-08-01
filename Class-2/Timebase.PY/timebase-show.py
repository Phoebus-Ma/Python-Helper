###
# Python dynamic print local time example.
# 
# License - MIT.
###

import os
import time


# Main function.
def main():
# {
    print('Press Ctrl + C to quit.')

    while True:
        show_time = time.asctime()
        print(show_time, end = '\r')

        time.sleep(1)
# }


# Program entry.
if '__main__' == __name__:
# {
    main()
# }
