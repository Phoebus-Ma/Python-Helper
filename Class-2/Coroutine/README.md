### Description

Coroutine test for python.


### Platform

Python 3 for Windows/Linux/MacOS.


### Feature

1. coroutine-yield.py       ---- Coroutine example using yield, python 2.7+.
2. coroutine-asyncio.py     ---- Coroutine example using asyncio, python 3.4+.
3. coroutine-async.py       ---- Coroutine example using async, python 3.5+.


### Example:

1. Coroutine yield test:

```console
$ python coroutine-yield.py

task 1: 0
task 2: 0
task 1: 1
task 2: 1
task 1: 2
task 2: 2
task 1: 3
Task 2 done.
task 1: 4
Task 1 done.
```

2. Coroutine async test:

```console
$ python coroutine-async.py

task 1: 0
task 2: 0
task 1: 1
task 2: 1
task 1: 2
task 2: 2
task 1: 3
Task 2 done.
task 1: 4
Task 1 done.
```
