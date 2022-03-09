###
# Thread event test.
# 
# License - MIT.
###

import time
from threading import Thread, Event


# thread_function - Thread test function.
def thread_function(num, pEvent):
# {
    while num > 0:
        print('num value: %d.' % num)
        num -= 1
        time.sleep(1)

    pEvent.set()
# }


# Main function.
def main():
# {
    thrd_event = Event()

    thrd = Thread(target = thread_function, args = (5, thrd_event))
    thrd.start()

    thrd_event.wait()

    print('The end.')
# }


# Program entry.
if '__main__' == __name__:
    main()
