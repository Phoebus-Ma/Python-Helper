### Description

Database test for python.


### Platform

Python 3 for Windows/Linux/MacOS.


### Feature

1. db-sqlite3.py        ---- Sqlite 3 database test example.
2. db-mongodb.py        ---- MongoDB database test example.
3. db-mysql.py          ---- MySQL database test example.


### Installation

1. Sqlite3

No, Python has sqlite3 built in.

2. MongoDB

2.1 Download and install MongoDB: https://www.mongodb.com/try/download/community .

2.2 Install MongoDB driver, Select the Python driver here: pip install pymongo .

3. MySQL

3.1 Download and install MySQL:  .


### Example:

1. Sqlite3 test:

```console
$ python db-sqlite3.py

Example 1 ------------------
Example 2 ------------------
Example 3 ------------------
Example 4 ------------------
Name:  Apple
Price: 10.0
Count: 100
Name:  Banana
Price: 2.5
Count: 123
Name:  Pear
Price: 1.8
Count: 256
Name:  Orange
Price: 2.0
Count: 300
Example 5 ------------------
Name:  Apple
Price: 9.8
Count: 100
Example 6 ------------------
Name:  Apple
Price: 9.8
Count: 100
Name:  Banana
Price: 2.5
Count: 123
Name:  Pear
Price: 1.8
Count: 256
Example 7 ------------------
Example 8 ------------------
('Supermarket',)
Example 9 ------------------
Example 10 ------------------
```

2. MongoDB test:

```console
$ python db-mongodb.py

--------Example 1--------
market
--------Example 2--------
fruits
--------Example 3--------
<pymongo.results.InsertOneResult object at 0x000001D4A3579940>
--------Example 4--------
<pymongo.results.InsertManyResult object at 0x000001D4A2E3DA00>
--------Example 5--------
[{'_id': ObjectId('6242b418ca97dd59cb19c9d4'), 'name': 'apricot', 'price': 2.1, 'count': 132}, {'_id': ObjectId('6242b419ca97dd59cb19c9d5'), 'name': 'apple', 'price': 10, 'count': 100}, {'_id': ObjectId('6242b419ca97dd59cb19c9d6'), 'name': 'banana', 'price': 2.5, 'count': 123}, {'_id': ObjectId('6242b419ca97dd59cb19c9d7'), 'name': 'pear', 'price': 1.8, 'count': 256}, {'_id': ObjectId('6242b419ca97dd59cb19c9d8'), 'name': 'orange', 'price': 2, 'count': 300}]
--------Example 6--------
{'_id': ObjectId('6242b419ca97dd59cb19c9d5'), 'name': 'apple', 'price': 10, 'count': 100}
--------Example 7--------
Database:  admin
Database:  config
Database:  local
Database:  market
--------Example 8--------
Collection:  fruits
--------Example 9--------
{'_id': ObjectId('6242b419ca97dd59cb19c9d5'), 'name': 'apple', 'price': 9.8, 'count': 110}
--------Example 10--------
5
--------Example 11--------
[{'_id': ObjectId('6242b418ca97dd59cb19c9d4'), 'name': 'apricot', 'price': 2.1, 'count': 132}, {'_id': ObjectId('6242b419ca97dd59cb19c9d5'), 'name': 'apple', 'price': 9.8, 'count': 110}, {'_id': ObjectId('6242b419ca97dd59cb19c9d6'), 'name': 'banana', 'price': 2.5, 'count': 123}, {'_id': ObjectId('6242b419ca97dd59cb19c9d7'), 'name': 'pear', 'price': 1.8, 'count': 256}]
--------Example 12--------
4
[]
--------Example 13--------
Not find collection.
--------Example 14--------
Database:  admin
Database:  config
Database:  local
```
