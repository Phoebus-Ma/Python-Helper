###
# TCP server use select example.
# 
# License - MIT.
###

import os
import sys
import time
import socket
from select import select


# Main function.
def main():
# {
    user_str = ''

    # Create socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get host ip address.
    host_name   = socket.gethostname()
    host_ip     = socket.gethostbyname(host_name)

    # Binding port, default max 65535.
    # Use host ip or 127.0.0.1
    sock.bind((host_ip, 65532))

    # Set the socket to non-blocking.
    sock.setblocking(False)

    # Listen port.
    sock.listen(8)

    # Set input/output list.
    rlist = [sock]
    wlist = []

    # Set select timeout.
    time_out = 10

    print('TCP Server running...')

    # Accept.
    while True:
    # {
        # The second rlist object is monitoring exception object.
        readable, writable, exceptionable = select(rlist, wlist, rlist, time_out)

        for s in readable:
        # {
            if s is sock:
                clt_sock, clt_addr = sock.accept()
                clt_sock.setblocking(0)
                print('Client %s:%s connect.' % clt_addr)

                rlist.append(clt_sock)
                wlist.append(clt_sock)

            else:
                try:
                    data = s.recv(1024)

                    if not data or 'exit' == data.decode('utf-8'):
                        if s in wlist:
                            wlist.remove(s)

                        rlist.remove(s)
                        s.close()

                        print('Client exit.')
                    
                    else:
                        print(data.decode('utf-8'))

                        if s not in wlist:
                            wlist.append(s)
                except:
                    print('Error in client.')
        # }

        for s in writable:
        # {
            try:
                s.send(b'OK')
                wlist.remove(s)

            except:
                wlist.remove(s)
        # }

        for s in exceptionable:
        # {
            if s in rlist:
                rlist.remove(s)

            if s in wlist:
                wlist.remove(s)
        # }
    # }

    # Close socket.
    sock.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
