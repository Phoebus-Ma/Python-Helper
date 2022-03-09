### Description
Multi-Process for python.

### Platform
Python 3 for Windows/Linux/MacOS.

### Feature
1. process.py       ---- Use multiprocessing create process, multi platform.
2. process-unix.py  ---- Use fork create process, runs only on unix-like platform.
3. process-pool.py  ---- Use process pool create process.
4. process-lock.py  ---- Use process locks to protect resources.
5. process-queue.py ---- Use queue for interprocess communication.
6. process-pipe.py  ---- Use pipe for interprocess communication.
7. process-manager.py ---- Use manager for interprocess communication.

### Example:
1. Process Test:
```console
$ python process.py

Parent process pid: 11564.
Child process pid: 9156, ppid: 11564, args: Hello, World.
```

2. Process Pool Test:
```console
$ python process-pool.py

This is process 0.
Done for process 0 ---------.
This is process 1.
This is process 2.
This is process 3.
Done for process 1 ---------.
This is process 4.
Done for process 2 ---------.
This is process 5.
Done for process 3 ---------.
This is process 6.
Done for process 4 ---------.
This is process 7.
Done for process 5 ---------.
This is process 8.
Done for process 6 ---------.
This is process 9.
Done for process 7 ---------.
Done for process 8 ---------.
Done for process 9 ---------.
Main process end.
```
