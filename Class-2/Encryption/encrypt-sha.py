###
# SHA1/SHA256/SHA384/SHA512 encryption example.
# 
# License - MIT.
####

import os
import hashlib


# SHA512 encryption.
def generate_sha512():
# {
    hsha = hashlib.sha512()

    hsha.update(test_str1.encode(encoding = 'UTF-8'))
    hsha.update(test_str2.encode(encoding = 'UTF-8'))

    print("SHA512 encrypt data:\t" + hsha.hexdigest())
# }


# SHA384 encryption.
def generate_sha384():
# {
    hsha = hashlib.sha384()

    hsha.update(test_str1.encode(encoding = 'UTF-8'))
    hsha.update(test_str2.encode(encoding = 'UTF-8'))

    print("SHA384 encrypt data:\t" + hsha.hexdigest())
# }


# SHA256 encryption.
def generate_sha256():
# {
    hsha = hashlib.sha256()

    hsha.update(test_str1.encode(encoding = 'UTF-8'))
    hsha.update(test_str2.encode(encoding = 'UTF-8'))

    print("SHA256 encrypt data:\t" + hsha.hexdigest())
# }


# SHA224 encryption.
def generate_sha224():
# {
    hsha = hashlib.sha224()

    hsha.update(test_str1.encode(encoding = 'UTF-8'))
    hsha.update(test_str2.encode(encoding = 'UTF-8'))

    print("SHA224 encrypt data:\t" + hsha.hexdigest())
# }


# SHA1 encryption.
def generate_sha1():
# {
    hsha = hashlib.sha1()

    hsha.update(test_str1.encode(encoding = 'UTF-8'))
    hsha.update(test_str2.encode(encoding = 'UTF-8'))

    print("SHA1 encrypt data:\t" + hsha.hexdigest())
# }


# Main function.
def main():
# {
    # SHA1 test.
    generate_sha1()

    # SHA224 test.
    generate_sha224()

    # SHA256 test.
    generate_sha256()

    # SHA384 test.
    generate_sha384()

    # SHA512 test.
    generate_sha512()
# }


# Program entry.
if '__main__' == __name__:
# {
    test_str1 = "Hello, World."
    test_str2 = "To be No.1"

    main()
# }
