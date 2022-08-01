###
# Multiprocessing queue test.
#
# License - MIT.
###

import os
import time
from multiprocessing import Process, Queue


# process_get_function - Get message test function.
def process_get_function(param):
# {
    queue = param

    while True:
        value = queue.get(True)
        print('Get data: %s.' % value)

        if ('Good' == value):
            break

        time.sleep(1)
# }


# process_put_function - Set message test function.
def process_put_function(param):
# {
    queue = param

    for value in ['Cool', 'Happy', 'Good']:
        print('Put data: %s.' % value)
        queue.put(value)

        time.sleep(1)
# }


# Main function.
def main():
# {
    # Create queue object.
    proc_queue = Queue()

    # Create test process.
    proc_get = Process(target = process_get_function, args = (proc_queue, ))
    proc_put = Process(target = process_put_function, args = (proc_queue, ))

    # Runs
    proc_get.start()
    proc_put.start()

    # Wait child process done.
    proc_get.join()
    proc_put.join()
# }


# Program entry.
if '__main__' == __name__:
    main()
