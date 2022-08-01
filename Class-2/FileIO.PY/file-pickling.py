###
# File serialization example.
# 
# License - MIT.
###

import os
import pickle


# Main function.
def main():
# {
    test_str = '(1 + 1 == 2), [Hello World], {2^10 == 2 << 10 == 1024}.'

    buffer = pickle.dumps(test_str)
    print(buffer)

    f = open('test.txt', 'wb')
    pickle.dump(test_str, f)
    f.close()

    f = open('test.txt', 'rb')
    buffer2 = pickle.load(f)
    f.close()
    print(buffer2)

    if os.path.exists('test.txt'):
        os.remove('test.txt')
# }


# Program entry.
if '__main__' == __name__:
    main()
