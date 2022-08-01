###
# DES encryption example.
# 
# License - MIT.
####

import os
import binascii

# [pip install pyDes].
from pyDes import des, CBC, PAD_PKCS5


# DES Encrypt.
def des_encrypt(src, passwd):
# {
    secret_key  = passwd
    IV          = secret_key

    desObj = des(secret_key, CBC, IV, pad = None, padmode = PAD_PKCS5)
    enData = desObj.encrypt(src, padmode = PAD_PKCS5)

    return binascii.b2a_hex(enData)
# }


# DES Decrypt.
def des_decrypt(src, passwd):
# {
    secret_key  = passwd
    IV          = secret_key

    desObj = des(secret_key, CBC, IV, pad = None, padmode = PAD_PKCS5)
    deData = desObj.decrypt(binascii.a2b_hex(src), padmode = PAD_PKCS5)

    return deData
# }


# Main function.
def main():
# {
    src_text = 'To be No.1'

    # Key must be exactly 8 bytes long.
    passwd = 'Hello,@1'

    # Encrypt.
    enData = des_encrypt(src_text, passwd)
    print(enData)

    # Decrypt.
    deData = des_decrypt(enData, passwd)
    print(deData)

    return 0
# }


# Program entry.
if '__main__' == __name__:
    main()
