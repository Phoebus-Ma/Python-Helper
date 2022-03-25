### Description

Compress/Uncompress test for python.


### Platform

Python 3 for Windows/Linux/MacOS.


### Feature

1. compress-zip.py      ---- Zip compress/uncompress example.
2. compress-tar.py      ---- Tar compress/uncompress example.
3. compress-7z.py       ---- 7zip compress/uncompress example.
4. compress-gz.py       ---- Gzip compress/uncompress example.


### Example:

1. Compress zip test:

```console
$ python compress-zip.py

Compressing compress-7zr.py
Compressing compress-gz.py
Compressing compress-tar.py
Compressing compress-zip.py
Compressing README.md
filename:        README.md
data_time:       (2022, 3, 23, 13, 45, 28)
compress_type:   8
compress_size:   171
file_size:       326
### Description

Compress/Uncompress test for python.

... ...

Decompressed file successfully.
Compressing .\compress-7zr.py
Compressing .\compress-gz.py
Compressing .\compress-tar.py
Compressing .\compress-zip.py
Compressing .\README.md
Compressing .\test.zip
Compressing .\et_test\compress-7zr.py
Compressing .\et_test\compress-gz.py
Compressing .\et_test\compress-tar.py
Compressing .\et_test\compress-zip.py
Compressing .\et_test\README.md
```

2. Compress tar test:

```console
$ python compress-tar.py

Compress.PY
Compress.PY/README.md
Compress.PY/compress-7zr.py
Compress.PY/compress-gz.py
Compress.PY/compress-tar.py
Compress.PY/compress-zip.py
Compress.PY/dir_test.zip
Compress.PY/et_test
Compress.PY/et_test/README.md
Compress.PY/et_test/compress-7zr.py
Compress.PY/et_test/compress-gz.py
Compress.PY/et_test/compress-tar.py
Compress.PY/et_test/compress-zip.py
Compress.PY/test.zip
name Compress.PY/README.md
size 1063
mtime 1648177033
```
