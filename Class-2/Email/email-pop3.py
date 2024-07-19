###
# Python POP3 receive email test example.
# 
# License - MIT
###

import os
import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


# Main function.
def main():
# {
    user_name = input('Username: ')
    pass_word = input('Password: ')


    server = poplib.POP3(pop3_server)
    server.set_debuglevel(1)

    print(server.getwelcome().decode('utf-8'))

    server.user(user_name)
    server.pass_(pass_word)

    print('Messages: %s. Size: %s' % server.stat())
    resp, mails, octets = server.list()
    print(mails)

    index = len(mails)
    resp, lines, octets = server.retr(index)

    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)

    # server.dele(index)
    server.quit()
# }


# Program entry.
if '__main__' == __name__:
# {
    pop3_server = 'pop.126.com'

    main()
# }
