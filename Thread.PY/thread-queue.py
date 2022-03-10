###
# Thread queue test.
# 
# License - MIT.
###

import time
from queue import Queue
from threading import Thread


# thread_producer - Producer Model.
def thread_producer(thrd_queue):
# {
    for i in range(32):
        thrd_queue.put(i)

        print('-----------------%d' % i)

        time.sleep(0.1)
# }


# thread_consumer - Consumer Model.
def thread_consumer(id, thrd_queue):
# {
    while True:
        intValue = thrd_queue.get()

        if (16 < intValue):
            break

        print('ID: %d, Num: %d.' % (id, intValue))
# }


# Main function.
def main():
# {
    thrd_queue = Queue(32)

    thrd1 = Thread(target = thread_producer, args = (thrd_queue, ))
    thrd2 = Thread(target = thread_consumer, args = (2, thrd_queue))
    thrd3 = Thread(target = thread_consumer, args = (3, thrd_queue))

    thrd2.start()
    thrd1.start()
    thrd3.start()

    thrd1.join()
    thrd2.join()
    thrd3.join()

    print('The end.')
# }


# Program entry.
if '__main__' == __name__:
    main()

