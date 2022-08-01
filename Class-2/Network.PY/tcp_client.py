###
# TCP client example.
# 
# License - MIT.
###

import os
import socket


# Main function.
def main():
# {
    # Create socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get host ip address.
    host_name   = socket.gethostname()
    host_ip     = socket.gethostbyname(host_name)

    # Connect server.
    sock.connect((host_ip, 65532))

    # Reveive server ack.
    data = sock.recv(1024)
    print(data.decode('utf-8'))

    # Communication.
    for i in range(5):
        sock.send(b'Hello')

        # Receive ack.
        print(sock.recv(1024).decode('utf-8'))

    # Disconnect server.
    sock.send(b'exit')
    sock.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
