###
# Thread condition test.
# 
# License - MIT.
###

from ast import arg
import time
from threading import Thread, Condition


# thread_customer - bus customer.
def thread_customer(condition):
# {
    time.sleep(1)

    # Step 2.
    condition.acquire()
    print('2. Customer take the bus.')

    condition.notify()

    # Step 4.
    condition.wait()
    print('4. Pay for the tickets, sit down.')

    condition.notify()
    condition.release()
# }


# thread_driver - bus driver.
def thread_driver(condition):
# {
    # Step 1.
    condition.acquire()
    print('1. Bus to station, open the doors.')

    # Step 3.
    condition.wait()
    print('3. Close the doors.')

    condition.notify()

    # Step 5
    condition.wait()
    print('5. Go forward.')

    condition.release()
# }


# Main function.
def main():
# {
    # Create Condition
    cond = Condition()

    # Create Threads.
    thrd1 = Thread(target = thread_driver, args = (cond, ))
    thrd2 = Thread(target = thread_customer, args = (cond, ))

    thrd1.start()
    thrd2.start()

    thrd1.join()
    thrd2.join()

    print('The End.')
# }


# Program entry.
if '__main__' == __name__:
    main()

