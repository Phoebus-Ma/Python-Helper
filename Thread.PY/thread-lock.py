###
# Thread lock test.
# 
# License - MIT.
###

import os
import threading


# Global var value.
tmp_value = 0


# change_value - Change global value.
def change_value(id):
# {
    global tmp_value

    tmp_value += id

    print('id: %d, Value: %d' % (id, tmp_value))
# }


# thread_function - Thread test function.
def thread_function(lock, id):
# {
    with lock:
        for i in range(10):
            change_value(id)
# }


# Main function.
def main():
# {
    # Create thread lock.
    lock = threading.Lock()

    thrd1 = threading.Thread(target = thread_function, args = (lock, 1))
    thrd2 = threading.Thread(target = thread_function, args = (lock, 2))

    thrd1.start()
    thrd2.start()

    thrd1.join()
    thrd2.join()

    print('The end, tmp_value: %d.' % tmp_value)
# }


# Program entry.
if '__main__' == __name__:
    main()
