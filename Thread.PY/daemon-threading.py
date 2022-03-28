###
# Python daemon thread test example by threading.
# 
# License - MIT.
###

import os
import time
import threading


# thread_function1 - Thread callback function.
def thread_function1():
# {
    i = 0

    try:
        while True:
            print('Daemon: %d' % i)
            i = i + 1

            time.sleep(1)
    except:
        pass
# }


# thread_function2 - Thread callback function.
def thread_function2():
# {
    for i in range(5):
        print('Normal: %d.' % i)
        time.sleep(1)

    print('Normal thread end.')
# }


# Main function.
def main():
# {
    print("main thread name: %s." % threading.current_thread().name)

    # Create a daemon child thread.
    thrd_daemon = threading.Thread(target = thread_function1, name = 'daemon_thread')
    # setDaemon() is deprecated, set the daemon attribute instead.
    thrd_daemon.daemon = True

    # Create a normal child thread.
    thrd_normal = threading.Thread(target = thread_function2, name = 'normal_thread')
    thrd_normal.daemon = False

    # Run sub-thread.
    thrd_daemon.start()
    thrd_normal.start()

    time.sleep(3)

    # Note:
    # The main thread exits, daemon child thread exits too.
    # Warning: Main thread ending is not necessarily quitting.
    print('Main thread end.')
# }


# Program entry.
if '__main__' == __name__:
    main()

