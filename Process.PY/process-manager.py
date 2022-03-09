###
# Multiprocessing manager test.
#
# License - MIT.
###

import os
from multiprocessing import Process, Manager, Lock


# process_function - Process test function.
def process_function(pLock, pDict):
# {
    with pLock:
        pDict['num'] -= 1
# }


# Main function.
def main():
# {
    lock = Lock()

    with Manager() as manager:
        proc_dict = manager.dict({"num" : 10})

        proc_list = []

        for i in range(10):
            process = Process(target = process_function, args = (lock, proc_dict))
            process.start()

            proc_list.append(process)

        for p in proc_list:
            p.join()
        
        print(proc_dict)
# }


# Program entry.
if '__main__' == __name__:
    main()
