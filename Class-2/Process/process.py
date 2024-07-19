###
# Multi process for multi platform.
#
# License - MIT.
###

import os
import time
from multiprocessing import Process


# process_function - Process callback function.
def process_function(param1, param2):
# {
    str1 = param1
    str2 = param2

    time.sleep(1)

    print('Child process pid: %s, ppid: %s, args: %s, %s.'
            % (os.getpid(), os.getppid(), str1, str2))
# }


# Main function.
def main():
# {
    print('Parent process pid: %s.' % (os.getpid()))

    # Create a child process.
    proc = Process(target = process_function, args = ("Hello", "World"))

    # Run child process.
    proc.start()

    # Wait for child process done.
    proc.join()
# }


# Program entry.
if '__main__' == __name__:
    main()
