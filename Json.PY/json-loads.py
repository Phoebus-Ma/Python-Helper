###
# Json decode example.
# 
# License - MIT.
####

import json


# Main function.
def main():
# {
    json_data = '{"count": 4, "data": {"key1": 1, "key2": 2.1, "key3": true, "key4": "nihao"}}'

    text_data = json.loads(json_data)

    # Json data convert to normal data.
    print(text_data)

    # Parse count.
    parse_count = text_data.get('count')
    print(parse_count)

    # Parse data.
    parse_data = text_data.get('data')
    print(parse_data)

    # Parse key1 by style 2.
    valueKey1 = parse_data['key1']
    print(valueKey1)

    # Parse key2 by style 1.
    valueKey2 = text_data['data']['key2']
    print(valueKey2)
# }


# Program entry.
if '__main__' == __name__:
    main()
