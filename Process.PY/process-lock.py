###
# Multiprocessing lock test.
#
# License - MIT.
###

import os
from multiprocessing import Process, Lock


# process_function - Process test function.
def process_function(id, lock):
# {
    lock.acquire()
    
    print('Process id: %d.' % id)

    lock.release()
# } 


# Main function.
def main():
# {
    # Create lock.
    proc_lock = Lock()

    for i in range(10):
        process = Process(target = process_function, args = (i, proc_lock))
        process.start()

    print('The end.')
# }


# Program entry.
if '__main__' == __name__:
    main()
