###
# UDP server example.
# 
# License - MIT.
###

import os
import socket


# Main function.
def main():
# {
    # Create socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get host ip address.
    host_name   = socket.gethostname()
    host_ip     = socket.gethostbyname(host_name)

    # Binding port.
    # Use host ip or 127.0.0.1
    sock.bind((host_ip, 65533))

    print('UDP Server running...')

    # Accept.
    while True:
        data, addr = sock.recvfrom(1024)
        if 'shutdown' == data.decode('utf-8'):
            break

        print('Client data: %s', data.decode('utf-8'))
        sock.sendto(b'OK', addr)
# }


# Program entry.
if '__main__' == __name__:
    main()
