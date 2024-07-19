###
# Python 2.7+, yield test.
# 
# License - MIT
###

import os
from collections import deque


# task_func2 - Test function 2.
def task_func2():
# {
    for i in range(3):
        print('task 2: %d' % i)

        # Switching task.
        yield

    print('Task 2 done.')
# }


# task_func1 - Test function 1.
def task_func1():
# {
    for i in range(5):
        print('task 1: %d' % i)

        # Switching task.
        yield

    print('Task 1 done.')
# }


# TaskScheduler - Task scheduler.
class TaskScheduler:
# {
    # Initialization.
    def __init__(self):
    # {
        self._task_queue = deque()
    # }


    # Add task to task scheduler.
    def add(self, task):
    # {
        self._task_queue.append(task)
    # }


    # Run the task scheduler.
    def run(self):
    # {
        while self._task_queue:
            task = self._task_queue.popleft()

            try:
                # .
                next(task)

                self._task_queue.append(task)
            except StopIteration:
                pass
    # }
# }


# Main function.
def main():
# {
    sched = TaskScheduler()

    sched.add(task_func1())
    sched.add(task_func2())

    sched.run()
# }


# Program entry.
if '__main__' == __name__:
    main()
