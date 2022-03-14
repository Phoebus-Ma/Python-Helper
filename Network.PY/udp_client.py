###
# UDP client example.
# 
# License - MIT.
###

import os
import time
import socket


# Main function.
def main():
# {
    # Create socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get host ip address.
    host_name   = socket.gethostname()
    host_ip     = socket.gethostbyname(host_name)

    # Server address.
    addr = (host_ip, 65533)
    print('Client running...')

    # Commucation.
    for i in range(5):
        sock.sendto(b'Hello', addr)

        data = sock.recv(1024).decode('utf-8')
        print(data)

        time.sleep(1)

    # Disconnect server.
    sock.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
