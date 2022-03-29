###
# Python MongoDB test example.
# 
# License - MIT.
###

import os

# pip install pymongo.
import pymongo


# Main function.
def main():
# {
    test_data1 = {'name': 'apricot', 'price': 2.1, 'count': 132}

    test_data2 = [
        {'name': 'apple',   'price': 10,    'count': 100},
        {'name': 'banana',  'price': 2.5,   'count': 123},
        {'name': 'pear',    'price': 1.8,   'count': 256},
        {'name': 'orange',  'price': 2,     'count': 300}
    ]

    # Connect to mongodb.
    clt_mongo = pymongo.MongoClient('localhost', 27017)

    # Example 1: Create database.
    print('--------Example 1--------')
    db_market = clt_mongo['market']
    print(db_market.name)

    # Example 2: Create collection.
    print('--------Example 2--------')
    col_fruits = db_market['fruits']
    print(col_fruits.name)

    # Example 3: Insert one data to collection.
    print('--------Example 3--------')
    ret = col_fruits.insert_one(test_data1)
    print(ret)

    # Example 4: Insert many data to collection.
    print('--------Example 4--------')
    ret = col_fruits.insert_many(test_data2)
    print(ret)

    # Example 5: show all data.
    print('--------Example 5--------')
    datas = col_fruits.find()
    print(list(datas))

    # Example 6: show one data.
    print('--------Example 6--------')
    data = col_fruits.find_one({'name': 'apple'})
    print(data)

    # Example 7: Show dbs.
    print('--------Example 7--------')
    db_list = clt_mongo.list_database_names()

    for db_name in db_list:
        print('Database: ', db_name)

    # Example 8: Show collections.
    print('--------Example 8--------')
    col_list = db_market.list_collection_names()

    for col_name in col_list:
        print('Collection: ', col_name)

    # Example 9: Edit data.
    print('--------Example 9--------')
    col_fruits.update_one({'name': 'apple'}, {'$set': {'price': 9.8, 'count': 110}})

    data = col_fruits.find_one({'name': 'apple'})
    print(data)

    # Example 10: document count.
    print('--------Example 10--------')
    count = col_fruits.estimated_document_count()
    print(count)

    # Example 11: delete one data.
    print('--------Example 11--------')
    col_fruits.delete_one({'name': 'orange'})

    datas = col_fruits.find()
    print(list(datas))

    # Example 12: delete all data.
    print('--------Example 12--------')
    ret = col_fruits.delete_many({})
    print(ret.deleted_count)

    datas = col_fruits.find()
    print(list(datas))

    # Example 13: delete collection.
    print('--------Example 13--------')
    db_market.drop_collection(col_fruits)

    col_list = db_market.list_collection_names()

    if 0 == len(col_list):
        print('Not find collection.')
    else:
        for col_name in col_list:
            print('Collection: ', col_name)

    # Example 14: delete database.
    print('--------Example 14--------')
    clt_mongo.drop_database(db_market)

    db_list = clt_mongo.list_database_names()

    for db_name in db_list:
        print('Database: ', db_name)

    # Close database.
    clt_mongo.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
