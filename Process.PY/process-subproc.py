###
# Python subprocess test example.
# 
# License - MIT.
###

import os
import sys
import subprocess


# subproc_popen - .
def subproc_popen():
# {
    if 'win32' == sys.platform:
        subprocess.Popen('notepad.exe')
    elif 'linux' == sys.platform:
        subprocess.Popen(['/bin/sh', '-c', 'ls -l'])
    elif 'darwin' == sys.platform:
        subprocess.Popen(['/bin/sh', '-c', 'ls -l'])

    cmd_str = 'ping 127.0.0.1'

    if 'nt' == os.name:
        cmd_str = cmd_str + ' -n 4'
    elif 'posix' == os.name:
        cmd_str = cmd_str + ' -c 4'
    else:
        cmd_str = 'ping -h'

    pcmd = subprocess.Popen(
        cmd_str.split(),
        stdin  = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    # Input, output, error.
    output, error = pcmd.communicate()

    # Get current encoding.
    sys_decode = sys.stdout.encoding

    # Output message.
    print('Msg: ', output.decode(sys_decode))
    print('Exit code: ', pcmd.returncode)
# }


# subproc_cmd - Shell command.
def subproc_cmd():
# {
    try:
        subprocess.run(['python', '--version'])
    except:
        pass

    return 0
# }


# Main function.
def main():
# {
    # Example 1: Shell command.
    subproc_cmd()

    # Example 2: .
    subproc_popen()

    return 0
# }


# Program entry.
if '__main__' == __name__:
    main()
