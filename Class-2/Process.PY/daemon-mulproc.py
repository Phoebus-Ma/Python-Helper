###
# Daemon process for multi platform.
#
# License - MIT.
###

import os
import time
from multiprocessing import Process


# process_function1 - Process callback function.
def process_function1(param):
# {
    i = 0

    while True:
        print('D: %d' % i)
        i = i + 1

        time.sleep(1)
# }


# process_function2 - Process callback function.
def process_function2(param):
# {
    str1 = param

    print('Starting: %s' % str1)

    for i in range(5):
        print('N: %d.' % i)
        time.sleep(1)

    print('Exiting: %s' % str1)
# }


# Main function.
def main():
# {
    print('Parent process pid: %s.' % (os.getpid()))

    # Create a daemon child process.
    proc_daemon = Process(target = process_function1, args = ("Daemon", ))
    proc_daemon.daemon = True

    # Create a normal child process.
    proc_normal = Process(target = process_function2, args = ("Normal", ))
    proc_normal.daemon = False

    # Run child process.
    proc_daemon.start()
    proc_normal.start()

    time.sleep(3)

    # Note:
    # The parent process exits, daemon child process exits too.
    # Warning: Parent process ending is not necessarily quitting.
    print('Parent end.')
# }


# Program entry.
if '__main__' == __name__:
    main()
