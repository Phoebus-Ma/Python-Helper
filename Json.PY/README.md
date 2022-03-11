### Description
Json test for python.

### Platform
Python 3 for Windows/Linux/MacOS.

### Feature
3. json-dumps.py    ---- Use json dump, transition normal data to json data.
4. json-loads.py    ---- Use json loads, transition json data to normal data.

### Example:
1. Json dump Test:
```console
$ python json-dumps.py

{'key3': True, 'key4': 'nihao', 'key2': 2.1, 'key1': 1}
----------------
{"key3": true, "key4": "nihao", "key2": 2.1, "key1": 1}
{"key1": 1, "key2": 2.1, "key3": true, "key4": "nihao"}

{'A': 1, 'B': True, 3: 2.2, 4: 'Hello', 5: [1, True, 'happy']}
----------------
{"A": 1, "B": true, "3": 2.2, "4": "Hello", "5": [1, true, "happy"]}
```

2. json loads Test:
```console
$ python json-loads.py

{'count': 4, 'data': {'key1': 1, 'key2': 2.1, 'key3': True, 'key4': 'nihao'}}
4
{'key1': 1, 'key2': 2.1, 'key3': True, 'key4': 'nihao'}
1
2.1
```
