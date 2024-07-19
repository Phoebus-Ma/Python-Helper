###
# TCP server use multi process example.
# 
# License - MIT.
###

import os
import time
import socket
from multiprocessing import Process


# Process.
def process_function(sock, addr):
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

    # Binding port.
    # Use host ip or 127.0.0.1
    sock.bind((host_ip, 65532))

    # Listen port, default max 65535.
    sock.listen(8)
    print('TCP Server running...')

    # Accept.
    while True:
        sck, addr = sock.accept()
        print('Client %s:%s connect.' % addr)

        # Create sub Process.
        proc = Process(target = process_function, args = (sck, addr))
        proc.start()
# }


# Program entry.
if '__main__' == __name__:
    main()
