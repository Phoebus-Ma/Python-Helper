###
# Json decode example.
# 
# License - MIT.
####

import json


# Main function.
def main():
# {
    json_data = '{"key1": 1, "key2": 2.2, "key3": "A", "key4": "nihao"}'

    text_data = json.loads(json_data)

    print(text_data)
# }


# Program entry.
if '__main__' == __name__:
    main()
