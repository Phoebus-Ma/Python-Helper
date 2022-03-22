###
# Python 3.4+, asyncio/yield from test.
# 
# License - MIT
###

import os
import asyncio


# task_func2 - Test function 2.
@asyncio.coroutine
def task_func2():
# {
    for i in range(3):
        print('task 2: %d' % i)

        # Switching task.
        yield from asyncio.sleep(1)

    print('Task 2 done.')
# }


# task_func1 - Test function 1.
@asyncio.coroutine
def task_func1():
# {
    for i in range(5):
        print('task 1: %d' % i)

        # Switching task.
        yield from asyncio.sleep(1)

    print('Task 1 done.')
# }


# Main function.
def main():
# {
    task_list = [
        task_func1(),
        task_func2()
    ]

    switer = asyncio.get_event_loop()
    switer.run_until_complete(asyncio.wait(task_list))

    switer.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
