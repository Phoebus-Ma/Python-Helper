###
# Python SMTP send email test example.
# 
# License - MIT
###

import os
import smtplib

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr, formataddr


# Format address.
def _format_addr(s):
# {
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# }


# Main function.
def main():
# {
    smtp_server = 'smtp.126.com'

    # Email user information.
    print('Login for email.')
    user_name   = input('Username: ')
    pass_word   = input('Password: ')

    # Email Recipient.
    recipient   = input('Recipient: ')

    # Send context.
    send_text       = 'To be No.1 .'

    msg             = MIMEText(send_text, 'plain', 'utf-8')
    msg['From']     = _format_addr('Handsome <%s>' % user_name)
    msg['To']       = _format_addr('Superman <%s>' % recipient)
    msg['Subject']  = Header('Hello World.', 'utf-8').encode()

    # server = smtplib.SMTP(smtp_server, 25)
    server = smtplib.SMTP_SSL(smtp_server, port = 465)

    server.set_debuglevel(1)
    server.login(user_name, pass_word)
    server.sendmail(user_name, [recipient], msg.as_string())

    server.quit()
# }


# Program entry.
if '__main__' == __name__:
# {
    main()
# }
