###
# Multi process for Unix-like platform.
#
# Runs only on Unix-like platform.
#
# License - MIT.
###

import os

# Main function.
def main():
# {
    pid = os.fork()

    if 0 == pid:
        print("Child process, pid: %s, ppid: %s." % (os.getpid(), os.getppid()))
    else:
        print("Parent process, pid: %s, child pid: %s" % (os.getpid(), pid))
# }


# Program entry.
if '__main__' == __name__:
    main()
