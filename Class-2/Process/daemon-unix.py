###
# Daemon process for Unix-like platform.
#
# License - MIT.
###

import os
import sys


# daemon_init - Create daemon process.
def daemon_init():
# {
    # Fork sub process, parent process exiting.
    ret = os.fork()

    if (-1 == ret):
        return -1
    elif (0 == ret):
        pass
    else:
        sys.exit(0)

    # Runs a program in a new session.
    if (-1 == os.setsid()):
        return -1

    # Change working directory.
    os.chdir('/')

    # Flush data.
    for f in sys.stdout, sys.stderr:
        f.flush()

    # Open the target file handle.
    std_in  = open(os.devnull, 'r')
    std_out = open(os.devnull, 'a+')

    # duplicate a file descriptor.
    os.dup2(std_in.fileno(), sys.stdin.fileno())
    os.dup2(std_out.fileno(), sys.stdout.fileno())

    try:
        std_err = open(os.devnull, 'a+', 0)
        os.dup2(std_err.fileno(), sys.stderr.fileno())
    except:
        pass

    return 0
# }


### -----------------------------------------------------------
# Main function.
# Runs on Unix-like platform.
# This routine has been tested on Ubuntu 20.
#
# $ ps -A
# $ python3 daemon-unix.py
# $ ps -A
# $ cat /tmp/hello_daemon.txt
# To be No.1.
# $ rm /tmp/hello_daemon.txt
### -----------------------------------------------------------
def main():
# {
    # Create daemon process.
    daemon_init()

    # No information is displayed on the terminal.
    for i in range(10):
        print('Hello')

        time.sleep(1)

    # Write a file.
    with open('/tmp/hello_daemon.txt', 'w') as f:
        f.write('To be No.1.\n')

    return 0
# }


# Program entry.
if '__main__' == __name__:
    main()
