### Description

Web test for python.


### Platform

Python 3 for Windows/Linux/MacOS.


### Feature

1. server-wsgi.py       ---- Web Server Gateway Interface (WSGI) test.
2. server-flask.py      ---- Web server use flask.
3. server-aiohttp.py    ---- Web server use aiohttp.
4. client-get.py        ---- Get web data and save html.
5. client-post.py       ---- Login github and get test url data.
6. client-aiohttp.py    ---- Get and Post test by aiohttp.


### Installation

```console
$ pip install flask
$ pip install aiohttp
```


### Example:

1. Web WSGI server test:
*After the server is started, enter 127.0.0.1:65531 in the browser.*

```console
$ python server-wsgi.py

Web server start!
Enter this URL in your browser: 127.0.0.1:65531.
Ctrl+C to stop the server.
127.0.0.1 - - [19/Mar/2022 23:30:18] "GET / HTTP/1.1" 200 22
127.0.0.1 - - [19/Mar/2022 23:30:18] "GET /favicon.ico HTTP/1.1" 200 22
```

2. Web Flask server test:

*To use this routine you should first install flask using PIP*.

```console
$ pip install flask
$ python server-flask.py

 * Serving Flask app 'server-flask' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 117-651-357
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [20/Mar/2022 17:21:28] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [20/Mar/2022 17:22:01] "POST /calclate_result/ HTTP/1.1" 200 -
127.0.0.1 - - [20/Mar/2022 17:22:07] "POST /calclate_result/ HTTP/1.1" 200 -
127.0.0.1 - - [20/Mar/2022 17:22:18] "POST /calclate_result/ HTTP/1.1" 200 -
127.0.0.1 - - [20/Mar/2022 17:22:22] "POST /calclate_result/ HTTP/1.1" 200 -
```
