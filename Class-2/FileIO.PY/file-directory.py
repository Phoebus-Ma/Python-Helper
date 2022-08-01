###
# Create/delete directory or file example.
# 
# License - MIT.
###

import os
import shutil


# Main function.
def main():
# {
    # Show system platform.
    print(os.name)

    # Show current absolution path.
    cur_dir = os.path.abspath('.')
    print(cur_dir)

    # Create a new directory.
    new_dir = os.path.join(cur_dir, 'test_folder')

    try:
        os.mkdir(new_dir)

        if True == os.path.exists(new_dir):
            print('Create directory success.')
    except:
        print('Directory already exist.')

    # Split path.
    open('test.txt', 'w').close()

    cur_file = os.path.abspath('test.txt')
    split_str = os.path.split(cur_file)

    print(split_str[0])
    print(split_str[1])

    # Splite expanded name.
    split_str2 = os.path.split(cur_file)
    print(split_str2[0])
    print(split_str2[1])

    # Rename file.
    try:
        os.rename('test.txt', 'hello.py')
    except:
        print('File already exists.')

    # Copy file.
    shutil.copy2('hello.py', 'happy.py')

    # Move file.
    try:
        shutil.move('happy.py', new_dir)
    except:
        print('Move file already exists.')

    # Delete file.
    try:
        new_file = os.path.join(new_dir, 'happy.py')
        os.remove(new_file)
        os.remove('hello.py')
    except:
        print("File does not exist.")

    # Delete directory.
    try:
        os.rmdir(new_dir)
    except:
        print('Directory does not exist.')
# }


# Program entry.
if '__main__' == __name__:
    main()
