###
# Python IMAP receive email test example.
# 
# License - MIT
###

import os
import imaplib
import pprint


# Main function.
def main():
# {
    print('Login QQ email:')
    imap_user = input('Username:')
    imap_pass = input('Password:')

    imap = imaplib.IMAP4_SSL(host = imap_host, port = 993)

    imap.login(imap_user, imap_pass)

    imap.select('Inbox')

    tmp, data = imap.search(None, 'ALL')

    for num in data[0].split():
        tmp, data = imap.fetch(num, '(RFC822)')
        print('Message: {0}\n'.format(num))
        # pprint.pprint(data[0][1])
        break

    imap.close()
    imap.logout()
# }


# Program entry.
if '__main__' == __name__:
# {
    imap_host = 'imap.qq.com'

    main()
# }
