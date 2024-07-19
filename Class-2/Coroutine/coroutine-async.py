###
# Python 3.5+, async/await test.
# 
# License - MIT
###

import os
import asyncio


# task_func2 - Test function 2.
async def task_func2():
# {
    for i in range(3):
        print('task 2: %d' % i)

        # Switching task.
        await asyncio.sleep(0)

    print('Task 2 done.')
# }


# task_func1 - Test function 1.
async def task_func1():
# {
    for i in range(5):
        print('task 1: %d' % i)

        # Switching task.
        await asyncio.sleep(0)

    print('Task 1 done.')
# }


# TaskScheduler - Task scheduler.
async def TaskScheduler():
# {
    await asyncio.gather(
        task_func1(),
        task_func2()
    )
# }


# Main function.
def main():
# {
    asyncio.run(TaskScheduler())
# }


# Program entry.
if '__main__' == __name__:
    main()
