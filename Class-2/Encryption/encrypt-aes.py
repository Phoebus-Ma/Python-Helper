###
# DES encryption example.
# 
# License - MIT.
####

import os
import binascii

# Windows platform: [pip install pycryptodome].
# Linux platform:   [pip3 install pycrypto].
from Crypto.Cipher import AES


# Make the data length a multiple of 16.
def aes_preprocessing(src):
# {
    if len(src.encode('UTF-8')) % 16:
        extData = 16 - (len(src.encode('UTF-8')) % 16)
    else:
        extData = 0

    src = src + ('\0' * extData)

    return src.encode('UTF-8')
# }


# AES Encrypt.
def aes_encrypt(src, passwd, passiv):
# {
    src = aes_preprocessing(src)

    aesObj = AES.new(passwd, AES.MODE_CBC, passiv)
    enData = aesObj.encrypt(src)

    return binascii.b2a_hex(enData)
# }


# AES Decrypt.
def aes_decrypt(src, passwd, passiv):
# {
    aesObj = AES.new(passwd, AES.MODE_CBC, passiv)
    deData = aesObj.decrypt(binascii.a2b_hex(src))

    return bytes.decode(deData).rstrip('\0')
# }


# Main function.
def main():
# {
    src_text = 'To be No.1'

    # Key must be exactly 16 bytes long.
    passwd = 'Hello,@1TobeNo.1'.encode('UTF-8')
    passiv = b'abc123def456,./?'

    # Encrypt.
    enData = aes_encrypt(src_text, passwd, passiv)
    print(enData)

    # Decrypt.
    deData = aes_decrypt(enData, passwd, passiv)
    print(deData)

    return 0
# }


# Program entry.
if '__main__' == __name__:
    main()
