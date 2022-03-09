###
# Thread semaphore test.
# 
# License - MIT.
###

from ast import arg
import queue
from threading import Thread, Semaphore
import time


# thread_function - Thread test function.
def thread_function(id, sema):
# {
    for i in range(5):
        with sema:
            print('Nihao thread id: %d.' % id)
            time.sleep(1)
# }


# Main function.
def main():
# {
    threads = []
    sema = Semaphore(3)

    for i in range(5):
        thrd = Thread(target = thread_function, args = (i, sema))
        thrd.start()
        threads.append(thrd)

    for thrd in threads:
        thrd.join()

    print('The end.')
# }


# Program entry.
if '__main__' == __name__:
    main()
