###
# Thread rlock test.
# 
# License - MIT.
###

import time
from threading import Thread, RLock


# thread_test2 - Thread test2 function.
def thread_test2(rlock):
# {
    time.sleep(0.5)

    rlock.acquire()
    print('Third acquire.')

    rlock.release()
# }


# thread_test1 - Thread test1 function.
def thread_test1(rlock):
# {
    rlock.acquire()
    print('First acquire.')

    rlock.acquire()
    print('Second acquire.')

    rlock.release()
    rlock.release()
# }


# Main function.
def main():
# {
    # Create RLock
    thrd_rlock = RLock()

    thrd1 = Thread(target = thread_test1, args = (thrd_rlock, ))
    thrd2 = Thread(target = thread_test2, args = (thrd_rlock, ))

    thrd1.start()
    thrd2.start()
# }


# Program entry.
if '__main__' == __name__:
    main()

