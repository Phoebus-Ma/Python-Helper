###
# Multiprocessing pipe test.
#
# License - MIT.
###

import os
from multiprocessing import Process, Pipe


# process_function - Process test function.
def process_function(pipe_connect):
# {
    pipe_connect.send('Hello')

    recv_data = pipe_connect.recv()
    print('Child process received: %s' % recv_data)
# }


# Main function.
def main():
# {
    # Create Pipe.
    parent_connect, child_connect = Pipe()

    process = Process(target = process_function, args = (child_connect, ))
    process.start()

    recv_data = parent_connect.recv()
    print('Main Received data: %s' % recv_data)

    parent_connect.send('Nihao')

    process.join()

    child_connect.close()
    parent_connect.close()
# }


# Program entry.
if '__main__' == __name__:
    main()
