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

Example for Windows:

3.1 Download MySQL zip file

    https://dev.mysql.com/downloads/mysql/

3.2 Unzip MySQL

    Such as: Unzip to path "D:\software\mysql"

3.3 Create .ini file

```bash
[client]
# Set default file format
default-character-set=utf8

[mysqld]
# Set port.
port = 3306

# Set MySQL unzip path
basedir=D:\\software\\mysql

# Set the maximum number of database connections.
max_connections=20

# Set server file format.
character-set-server=utf8

# The default storage engine to use when creating new tables.
default-storage-engine=INNODB
```

3.4 Run cmd.exe as admin

```console
$ D:
$ cd D:\software\mysql\bin
D:\software\mysql\bin> $ mysqld.exe --initialize --console

2022-03-29T08:15:08.949195Z 0 [System] [MY-013169] [Server] D:\software\mysql\bin\mysqld.exe (mysqld 8.0.28) initializing of server in progress as process 7204
2022-03-29T08:15:08.963463Z 0 [Warning] [MY-013242] [Server] --character-set-server: 'utf8' is currently an alias for the character set UTF8MB3, but will be an alias for UTF8MB4 in a future release. Please consider using UTF8MB4 in order to be unambiguous.
2022-03-29T08:15:09.129045Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2022-03-29T08:15:16.230495Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2022-03-29T08:15:29.018288Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: &y:r2tIwkglW

```

The "&y:r2tIwkglW" is MySQL Initial password.

```console
$ mysqld --initialize-insecure
$ mysqld install
$ net start mysql
The MySQL service is starting...
The MySQL service was started successfully.
```

```console
$ mysql -u root -p
Enter password: &y:r2tIwkglW
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.28

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> alter user user() identified by "123456";
Query OK, 0 rows affected (0.23 sec)

mysql> quit
Bye

```

The password already changed to 123456.

3.5 Python connect driver

3.5.1 mysql-connector-python

The "mysql-connector-python" is official driver.

`Note: if mysql version > 8, you need install "mysql-connector-python", not "mysql-connector"`

key_word: caching_sha2_password

```console
pip install mysql-connector-python
```

3.5.2 pymysql

```console
pip install pymysql
```

Either "mysql-connector" or "pymysql" will work.


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
