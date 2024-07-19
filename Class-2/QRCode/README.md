### Description

QRCode for python.


### Platform

Python 3 for Windows/Linux/MacOS.


### Install

1. Write.
```console
$ pip install qrcode
$ pip install pillow
```

2. Read.

1). zbar

```console
$ pip install pyzbar
```

On Windows x64:

Download and install `vcredist_x64.exe`

[vcredist_x64.exe](https://download.microsoft.com/download/2/E/6/2E61CFA4-993B-4DD4-91DA-3737CD5CD6E3/vcredist_x64.exe)


On Linux(Example for ubuntu):

```console
$ sudo apt install libzbar-dev -y
```


2). zxing

```console
$ pip install zxing
```

On Windows:


On Linux(Example for ubuntu):



### Feature

1. qr-write.py          ---- Create QR code picture.
2. qr-read.py           ---- Read QR information.


### Example:

1. QR write test:
```console
$ python qr-write.py

-----------Example 1-----------
Done 1.
-----------Example 1-----------
Done 2.
```

2. QR read test:
```console
$ python qr-read.py

```
