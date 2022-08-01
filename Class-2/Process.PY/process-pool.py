###
# Multiprocessing pool test.
#
# License - MIT.
###

import os
import time
from multiprocessing import Pool


# process_function - Process test function.
def process_function(param):
# {
    print('This is process %d.' % param)
    time.sleep(1 * param)
    print('Done for process %d ---------.' % param)
# }


# Main function.
def main():
# {
    # Max parallel running thread(s).
    proc_Pool = Pool(3)

    # Total threads.
    for i in range(10):
        proc_Pool.apply_async(process_function, args = (i, ))

    # Close pool.
    proc_Pool.close()

    # Wait for all child process done.
    proc_Pool.join()

    print('Main process end.')
# }


# Program entry.
if '__main__' == __name__:
    main()
