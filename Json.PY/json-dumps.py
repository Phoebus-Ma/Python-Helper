###
# Json decode example.
# 
# License - MIT.
####

import json


'''
This is can convert to json string:
1). dict
2). list
3). tuple
4). string
5). int
6). float
7). True
8). False
9). None
'''
# Main function.
def main():
# {
    test_data1 = {
        'key3' : True,
        'key4' : 'nihao',
        'key2' : 2.1,
        'key1' : 1,
    }

    test_data2 = {}

    test_data2['A'] = 1
    test_data2['B'] = True
    test_data2[3]   = 2.2
    test_data2[4]   = 'Hello'
    test_data2[5]   = [1, True, 'happy']

    test_data3 = json.dumps(test_data1)
    test_data4 = json.dumps(test_data1, sort_keys = True)
    test_data5 = json.dumps(test_data2)

    print(test_data1)
    print('----------------')
    print(test_data3)
    print(test_data4)

    print('')
    print(test_data2)
    print('----------------')
    print(test_data5)
# }


# Program entry.
if '__main__' == __name__:
    main()
