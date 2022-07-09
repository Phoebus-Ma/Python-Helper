###
# Python read qrcode information example.
# 
# License - MIT.
###

import os
from time import ctime
from urllib import response

# pip install ntplib
import ntplib


# Main function.
def main():
# {
    ntp_client = ntplib.NTPClient()

    response = ntp_client.request(ntp_address)

    print(ctime(response.tx_time))
# }


# Program entry.
if '__main__' == __name__:
# {
    # International.
    # ntp_address = 'pool.ntp.org'
    # ntp_address = 'time.windows.com'

    # China ntp.
    ntp_address = 'ntp.tencent.com'
    # ntp_address = 'ntp.aliyun.com'

    main()
# }
