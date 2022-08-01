###
# TCP server use multi thread example.
# 
# License - MIT.
###

import os
import time
import socket
from threading import Thread


# Thread.
def thread_function(sock, addr):
# {
    sock.send(b'Connected')

    while True:
        data = sock.recv(1024)

        if not data or 'exit' == data.decode('utf-8'):
            break

        sock.send(b'OK')
        print(data.decode('utf-8'))

        time.sleep(1)

    sock.close()
    print('Client %s:%s exit.' % addr)
# }


# Main function.
def main():
# {
    # Create socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get host ip address.
    host_name   = socket.gethostname()
    host_ip     = socket.gethostbyname(host_name)

    # Binding port, default max 65535.
    # Use host ip or 127.0.0.1
    sock.bind((host_ip, 65532))

    # Listen port.
    sock.listen(8)
    print('TCP Server running...')

    # Accept.
    while True:
        sck, addr = sock.accept()
        print('Client %s:%s connect.' % addr)

        # Create sub thread.
        thrd = Thread(target = thread_function, args = (sck, addr))
        thrd.start()
# }


# Program entry.
if '__main__' == __name__:
    main()
