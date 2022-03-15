### Description
Json test for network.

### Platform
Python 3 for Windows/Linux/MacOS.

### Feature
1. tcp-client.py    ---- TCP test client.
2. tcp-server.py    ---- Use multi thread tcp server.
3. tcp-server2.py   ---- Use multi process tcp server.
4. tcp-server3.py   ---- Use select tcp server.
5. udp-client.py    ---- UDP test client.
6. udp-server.py    ---- UDP server.

### Example:
1. Tcp server test:
```console
$ python tcp-server.py

TCP Server running...
Client 192.168.6.85:64341 connect.
Hello
Hello
Hello
Hello
Hello
Client 192.168.6.85:64341 exit.
```

2. Tcp client test:
```console
$ python tcp-client.py

Connected
OK
OK
OK
OK
OK
```
