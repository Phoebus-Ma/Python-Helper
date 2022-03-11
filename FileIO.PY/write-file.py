###
# Write file example.
# 
# License - MIT.
###

import os


# Verify read.
def verify_read():
# {
    f = open(testfile, 'r')

    data = f.read()
    print(data)

    f.close()
# }


# Write test 3.
def write_test3():
# {
    # Create.
    # 'x' - Create, create a file, returns an error if the file exist.
    # 'w' - Write, create a file if the specified file does not exist.
    # 'a' - Append, create a file if the specified file does not exist.
    create_file = 'myfile.txt'

    try:
        f = open(create_file, 'x')
        print('Create file success.')

        f.close()
    except:
        print('File exist.')

    if True == os.path.exists(create_file):
        print('Find the file.')
    else:
        print('No file found.')
# }


# Write test 2.
def write_test2():
# {
    # Overwrite.
    f = open(testfile, 'w')

    f.write('Do better every day.')

    f.close()
# }


# Write test 1.
def write_test1():
# {
    # Append.
    f = open(testfile, 'a')

    f.write('\nTo be no.1.')

    f.close()
# }


# Main function.
def main():
# {
    print('----Test 1----')
    write_test1()
    verify_read()

    print('----Test 2----')
    write_test2()
    verify_read()

    print('----Test 3----')
    write_test3()
# }


# Program entry.
if '__main__' == __name__:
    testfile = 'testfile.txt'
    main()
