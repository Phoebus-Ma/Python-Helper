###
# Python database test example.
# 
# License - MIT.
###

import os
import sqlite3


# sqlite3_helper - Sqlite 3 test example.
class sqlite3_helper:
# {
    # Initialization function.
    def __init__(self, dbname):
    # {
        self._dbname    = dbname
        self._connect   = sqlite3.connect(dbname)
        self._cursor    = None
    # }


    # open - Open database file.
    def open(self):
    # {
        self._cursor = self._connect.cursor()
    # }


    # close - Close database file.
    def close(self):
    # {
        self._connect.commit()
        self._connect.close()
    # }


    # execute - Execute database command.
    def execute(self, cmd):
    # {
        datas = None

        try:
            datas = self._cursor.execute(cmd)
        except:
            pass

        return datas
    # }


    # commit - Commit data to database.
    def commit(self):
    # {
        self._connect.commit()
    # }
# }


# Main function.
def main():
# {
    # Database name.
    db_name = 'test.db'

    ### ------------------------Section 1.------------------------ ###
    ###
    # Data type:
    # 1.NULL    : null value.
    # 2.INTEGER : A value is a signed integer stored in 1, 2, 3, 4, 6, or 8 bytes.
    # 3.REAL    : A value is a floating point value, stored as an 8-byte IEEE floating point number.
    # 4.TEXT    : The value is a text string stored using a database encoding (UTF-8, UTF-16BE, or UTF-16LE).
    # 5.BLOB    : A value is a BLOB of data stored entirely based on its input.
    ###

    # Command list.
    # 2.Create table.
    cmd_create_table = (
        '''
        create table Market
        (
            id      INTEGER primary key,
            name    TEXT,
            price   REAL,
            count   INTEGER,
            info    varchar(64)
        );
        '''
    )

    # 3.Insert data.
    cmd_insert_data = (
        # Data 1.
        '''
        insert into Market
        (id, name, price, count, info)
        values
        (1, 'Apple', 10, 100, 'Red round fruit')
        '''
        ,
        # Data 2.
        '''
        insert into Market
        (id, name, price, count, info)
        values
        (2, 'Banana', 2.5, 123, 'Yellow stick fruit')
        '''
        ,
        # Data 3.
        '''
        insert into Market
        (id, name, price, count, info)
        values
        (3, 'Pear', 1.8, 256, 'Yellow oval fruit')
        '''
        ,
        # Data 4.
        '''
        insert into Market
        (id, name, price, count, info)
        values
        (4, 'Orange', 2, 300, 'Orange round fruit')
        '''
    )

    # 4.Seartch data.
    cmd_search_data = (
        '''
        select
        name, price, count
        from
        Market
        '''
    )

    # 5.Update data.
    cmd_update_data = (
        '''
        update Market
        set price = 9.8
        where
        name="Apple"
        '''
    )

    # 6.Delete data.
    cmd_delete_data = (
        '''
        delete from Market where ID=4;
        '''
    )

    # 7.Rename table.
    cmd_remane_table = (
        '''
        alter table Market rename to Supermarket
        '''
    )

    # 8.Search table.
    cmd_search_table = (
        '''
        SELECT name FROM sqlite_master WHERE type = "table"
        '''
    )

    # 9.Delete table.
    cmd_delete_table = (
        '''
        drop table if exists Supermarket
        '''
    )


    ### ------------------------Section 2.------------------------ ###
    # Example 1: Create or connect database.
    print('Example 1 ------------------')
    sq_helper = sqlite3_helper(dbname = db_name)

    # Open sqlite3 database.
    sq_helper.open()

    # Example 2: Create db table.
    print('Example 2 ------------------')
    sq_helper.execute(cmd_create_table)

    # Example 3: Insert data.
    print('Example 3 ------------------')
    for i in range(len(cmd_insert_data)):
        sq_helper.execute(cmd_insert_data[i])

    sq_helper.commit()

    # Example 4: Search data.
    print('Example 4 ------------------')
    datas = sq_helper.execute(cmd_search_data)

    for data in datas:
        print('Name: ', data[0])
        print('Price:', data[1])
        print('Count:', data[2])

    # Example 5: Update data.
    print('Example 5 ------------------')
    sq_helper.execute(cmd_update_data)

    new_cmd = cmd_search_data + 'where name="Apple"'

    datas = sq_helper.execute(new_cmd)

    for data in datas:
        print('Name: ', data[0])
        print('Price:', data[1])
        print('Count:', data[2])

    # Example 6: Delete data.
    print('Example 6 ------------------')
    sq_helper.execute(cmd_delete_data)

    datas = sq_helper.execute(cmd_search_data)

    for data in datas:
        print('Name: ', data[0])
        print('Price:', data[1])
        print('Count:', data[2])

    # Example 7: Rename table.
    print('Example 7 ------------------')
    sq_helper.execute(cmd_remane_table)

    # Example 8: Search table.
    print('Example 8 ------------------')
    datas = sq_helper.execute(cmd_search_table)
    
    for name in datas:
        print(name)

    # # Example 9: Delete db table.
    print('Example 9 ------------------')
    sq_helper.execute(cmd_delete_table)

    datas = sq_helper.execute(cmd_search_table)

    for name in datas:
        print(name)

    # Close sqlite3 database.
    sq_helper.close()

    # Example 10: Delete db file.
    print('Example 10 ------------------')
    os.remove(db_name)
# }


# Program entry.
if '__main__' == __name__:
    main()
