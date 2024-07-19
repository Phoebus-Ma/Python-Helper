###
# Python thread test.
# 
# License - MIT
###

import os
import time
import threading


# thread_function - Thread test function.
def thread_function():
# {
    for i in range(5):
        print('%s running %d.' % (threading.current_thread().name, i))

        time.sleep(1)
# }


# Main function.
def main():
# {
    print("main thread name: %s." % threading.current_thread().name)

    thrd = threading.Thread(target = thread_function, name = 'thread_test')

    thrd.start()
    thrd.join()

    print('The end.')
# }


# Program entry.
if '__main__' == __name__:
    main()
