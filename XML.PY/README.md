### Description
Json test for XML.

### Platform
Python 3 for Windows/Linux/MacOS.

### Feature
1. sax-decode.py    ---- XML decode by SAX.
2. sax-encode.py    ---- XML encode by SAX.
3. dom-decode.py    ---- XML decode by DOM.
4. dom-encode.py    ---- XML encode by DOM.

### Example:
1. XML SAX decode test:
```console
$ python sax-decode.py

-------------------------
Title: Apple
price: 10
counts: 100
description: Red round fruit.
-------------------------
Title: Banana
price: 2.5
counts: 123
description: Yellow stick fruit.
-------------------------
Title: Pear
price: 1.8
counts: 256
description: Yellow oval fruit.
-------------------------
Title: Orange
price: 2
counts: 300
description: Orange round fruit.
```

2. XML SAX encode test:
```console
$ python sax-encode.py

Saved XML OK.
```
