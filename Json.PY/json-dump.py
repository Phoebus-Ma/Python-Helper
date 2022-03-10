###
# Json decode example.
# 
# License - MIT.
####

import json


# Main function.
def main():
# {
    test_data1 = {
        'key1' : 1,
        'key2' : 2.1,
        'key3' : 'A',
        'key4' : 'nihao',
    }

    test_data2 = json.dumps(test_data1)

    print(test_data2)
# }


# Program entry.
if '__main__' == __name__:
    main()
