### Description

Multi-thread for python.


### Platform

Python 3 for Windows/Linux/MacOS.


### Feature

1. thread.py            ---- Use threading create thread, multi platform.
2. thread-pool.py       ---- Use threading pool, this is third library.
3. thread-lock.py       ---- Use threading lock, Resource access with thread locks.
4. thread-queue.py      ---- Use threading and queue for interthread communication.
5. thread-event.py      ---- Use threading event for interthread communication.
6. thread-rlock.py      ---- Use threading rlock for interthread communication.
7. thread-semaphore.py  ---- Use threading semaphores for interthread communication.
8. thread-condition.py  ---- Use threading condition for interthread communication.
9. daemon-threading.py  ---- Use threading create daemon thread.


### Example:

1. Thread Test:
```console
$ python thread.py

main thread name: MainThread.
thread_test running 0.
thread_test running 1.
thread_test running 2.
thread_test running 3.
thread_test running 4.
The end.
```

2. Thread Lock Test:
```console
$ python thread-lock.py

id: 1, Value: 1
id: 1, Value: 2
id: 1, Value: 3
id: 1, Value: 4
id: 1, Value: 5
id: 1, Value: 6
id: 1, Value: 7
id: 1, Value: 8
id: 1, Value: 9
id: 1, Value: 10
id: 2, Value: 12
id: 2, Value: 14
id: 2, Value: 16
id: 2, Value: 18
id: 2, Value: 20
id: 2, Value: 22
id: 2, Value: 24
id: 2, Value: 26
id: 2, Value: 28
id: 2, Value: 30
The end, tmp_value: 30.
```
