### Description

Email for python.


### Platform

Python 3 for Windows/Linux/MacOS.


### Feature

1. email-stmp.py        ---- Send email by STMP(Simple Mail Transfer Protocol).
2. email-pop3.py        ---- Receive email by POP3(Post Office Protocol 3).
3. email-imap.py        ---- Receive email by IMAP(Internet Message Access Protocol).


### Example:

1. STMP Test:
```console
$ python email-stmp.py

Login for email.
Username: ************@126.com
Password: ************
Recipient: ************@intel.com
send: 'ehlo [255.255.255.255]\r\n'
reply: b'250-mail\r\n'
reply: b'250-PIPELINING\r\n'
reply: b'250-AUTH LOGIN PLAIN XOAUTH2\r\n'
reply: b'250-AUTH=LOGIN PLAIN XOAUTH2\r\n'
reply: b'250-coremail 1Uxr2xKj7kG********************************0xDrUUUUj\r\n'
reply: b'250-STARTTLS\r\n'
reply: b'250-ID\r\n'
reply: b'250 8BITMIME\r\n'
reply: retcode (250); Msg: b'mail\nPIPELINING\nAUTH LOGIN PLAIN XOAUTH2\nAUTH=LOGIN PLAIN XOAUTH2\ncoremail 1Uxr2xKj7kG********************************0xDrUUUUj\nSTARTTLS\nID\n8BITMIME'
send: 'AUTH PLAIN AHRpYW5qa****************PRFdDWEQ=\r\n'
reply: b'235 Authentication successful\r\n'
reply: retcode (235); Msg: b'Authentication successful'
send: 'mail FROM:<************@126.com>\r\n'
reply: b'250 Mail OK\r\n'
reply: retcode (250); Msg: b'Mail OK'
send: 'rcpt TO:<************@intel.com>\r\n'
reply: b'250 Mail OK\r\n'
reply: retcode (250); Msg: b'Mail OK'
send: 'data\r\n'
reply: b'354 End data with <CR><LF>.<CR><LF>\r\n'
reply: retcode (354); Msg: b'End data with <CR><LF>.<CR><LF>'
data: (354, b'End data with <CR><LF>.<CR><LF>')
send: b'Content-Type: text/plain; charset="utf-8"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: base64\r\nFrom: =?utf-8?q?Handsome?= <:<************@126.com>\r\nTo: =?utf-8?q?Superman?= <:<************@intel.com>\r\nSubject: =?utf-8?q?Hello_World=2E?=\r\n\r\nVG8gYmUgTm8uMSAu\r\n.\r\n'
reply: b'250 Mail OK queued as smtp9,NeRpCgBne8********GLFg--.64937S2 1656382331\r\n'
reply: retcode (250); Msg: b'Mail OK queued as smtp9,NeRpCgBne****7pifUGLFg--.6***7S2 1656***331'
data: (250, b'Mail OK queued as smtp9,NeRpCgBne****7pifUGLFg--.6***7S2 1656***331')
send: 'quit\r\n'
reply: b'221 Bye\r\n'
reply: retcode (221); Msg: b'Bye'
```

2. POP3 Test:
```console
$ python email-pop3.py

Username: ************@126.com
Password: ************
+OK Welcome to coremail Mail Pop3 Server (126coms[********************************])
*cmd* 'USER ************@126.com'
*cmd* 'PASS ************'
*cmd* 'STAT'
*stat* [b'+OK', b'17', b'654749']
Messages: 17. Size: 654749
*cmd* 'LIST'
[b'1 17478', b'2 11125', b'3 129533', b'4 58847', b'5 2928', b'6 55407', b'7 48941', b'8 98937', b'9 6436', b'10 72782', b'11 87792', b'12 3400', b'13 6439', b'14 16842', b'15 2672', b'16 6312', b'17 28878']
*cmd* 'RETR 17'
*cmd* 'QUIT'
```
