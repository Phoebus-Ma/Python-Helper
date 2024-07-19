###
# Python MySQL test example.
# 
# License - MIT.
###

import os

# pip install mysql-connector-python.
import mysql.connector


# mysql_create_db - Create database.
def mysql_create_db(db_address, db_username, db_password):
# {
    # Connect mysql.
    db_mysql = mysql.connector.connect(
        host        = db_address,
        port        = 3306,
        user        = db_username,
        password    = db_password,
        charset     = 'utf8',
    )

    db_cursor = db_mysql.cursor()

    # Example 1: Show databases.
    print('--------Example 1--------')
    db_cursor.execute('show databases')

    for data in db_cursor:
        print(data)

    # Example 2: Create database.
    print('--------Example 2--------')
    sql_cmd = 'create database if not exists market'

    try:
        db_cursor.execute(sql_cmd)
    except:
        pass

    db_cursor.execute('show databases')

    for data in db_cursor:
        print(data)

    db_cursor.close()
    db_mysql.close()
# }


# mysql_delete_db - Delete database.
def mysql_delete_db(db_address, db_username, db_password):
# {
    # Example 11: Delete database.
    print('--------Example 11--------')
    sql_cmd = 'drop database market'

    db_mysql = mysql.connector.connect(
        host        = db_address,
        port        = 3306,
        user        = db_username,
        password    = db_password,
        charset     = 'utf8',
    )

    db_cursor = db_mysql.cursor()

    db_cursor.execute(sql_cmd)

    db_cursor.execute('show databases')
    for data in db_cursor:
        print(data)

    db_cursor.close()
    db_mysql.close()
# }


# mysql_operator - insert, update, search, delete.
def mysql_operator(db_address, db_username, db_password):
# {
    # Example 3: Use database.
    print('--------Example 3--------')
    db_mysql = mysql.connector.connect(
        host        = db_address,
        port        = 3306,
        user        = db_username,
        password    = db_password,
        charset     = 'utf8',
        database    = 'market'
    )

    db_cursor = db_mysql.cursor()

    # Example 4: Show tables.
    print('--------Example 4--------')
    db_cursor.execute('show tables')

    for data in db_cursor:
        print(data)

    # Example 5: Create table.
    print('--------Example 5--------')
    sql_cmd = (
        '''
        create table if not exists fruits(
            id INT AUTO_INCREMENT,
            name VARCHAR(32),
            price REAL,
            count INT,
            description VARCHAR(64),
            PRIMARY KEY (id)
        )ENGINE = InnoDB DEFAULT CHARSET = utf8;
        '''
    )

    db_cursor.execute(sql_cmd)

    db_cursor.execute('show tables')
    for data in db_cursor:
        print(data)

    # Example 6: Insert data.
    print('--------Example 6--------')
    sql_cmd = (
        '''
        insert into fruits (name, price, count, description)
        values
        ('apple',  10.0, 100, 'Red round fruit')
        '''
        ,
        '''
        insert into fruits (name, price, count, description)
        values
        ('banana', 2.5,  123, 'Yellow stick fruit')
        '''
    )

    db_cursor.execute(sql_cmd[0])
    db_cursor.execute(sql_cmd[1])

    # Example 7: Search data.
    print('--------Example 7--------')
    sql_cmd = 'select * from fruits'
    sql_cmd2 = 'select * from fruits where name = "apple"'

    db_cursor.execute(sql_cmd)
    for data in db_cursor:
        print(data)

    db_cursor.execute(sql_cmd2)
    for data in db_cursor:
        print(data)

    # Example 8: Update data.
    print('--------Example 8--------')
    sql_cmd = 'update fruits set price = 9.8, count = 110 where name = "apple"'
    db_cursor.execute(sql_cmd)

    db_cursor.execute('select * from fruits')
    for data in db_cursor:
        print(data)

    # Example 9: Delete data.
    print('--------Example 9--------')
    sql_cmd = 'delete from fruits where name = "apple"'
    sql_cmd2 = 'delete from fruits'

    # delete one data.
    db_cursor.execute(sql_cmd)

    db_cursor.execute('select * from fruits')
    for data in db_cursor:
        print(data)

    # delete all data.
    db_cursor.execute(sql_cmd2)

    db_cursor.execute('select * from fruits')
    for data in db_cursor:
        print(data)

    # Example 10: Delete tables.
    print('--------Example 10--------')
    sql_cmd = 'drop table if exists fruits'

    db_cursor.execute(sql_cmd)

    db_cursor.execute('show tables')
    for data in db_cursor:
        print(data)

    db_cursor.close()
    db_mysql.close()
# }

# Main function.
def main():
# {
    ##
    # db_address  = localhost
    # db_username = root
    # db_password = 123456 or ${YourPassword}
    ##
    db_address  = input('Input database address: ')
    db_username = input('Input database username: ')
    db_password = input('Input database password: ')

    # Test 1.
    mysql_create_db(db_address, db_username, db_password)

    # Test 2.
    mysql_operator(db_address, db_username, db_password)

    # Test 3.
    mysql_delete_db(db_address, db_username, db_password)
# }


# Program entry.
if '__main__' == __name__:
    main()
