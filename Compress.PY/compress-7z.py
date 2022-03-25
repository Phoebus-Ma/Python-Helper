###
# Python 7zip compress/umcompress example.
# 
# License - MIT.
###

import os

# pip install py7zr
import py7zr


# p7z_all_umcompress - Uncompress the all file.
def p7z_all_umcompress(opt_style):
# {
    file_list = []

    # Open 7z file.
    p7zfile = py7zr.SevenZipFile(p7z_name, 'r', password = p7z_passwd)
    print('Need password', p7zfile.needs_password())

    # Bug:
    # If the name of the compressed file begins with a ".",
    # the "." will disappear when uncompressed.
    if (True == opt_style):
        datas = p7zfile.getnames()

        for et_file in datas:
            print('Uncompressing', et_file)
            file_list.append(et_file)

        p7zfile.extract(path = extract_path, targets = file_list)
    else:
        p7zfile.extractall(path = extract_path)
        print('Decompressed file successfully.')    

    p7zfile.close()
# }


# p7z_file_uncompress - Uncompress the specified file.
def p7z_file_uncompress():
# {
    with py7zr.SevenZipFile(p7z_name, 'r', password = p7z_passwd) as p7zfile:
        p7zfile.extract(path = extract_path + '_1', targets = file_name)
# }


# p7z_file_compress - Compress all file by file list.
def p7z_file_compress(need_pw, passwd):
# {
    # File list.
    file_list = []

    # Set current directory path.
    dirpath = '.'

    # Get current path all file.
    for path, dirnames, filenames in os.walk(dirpath):
        for file_name in filenames:
           file_list.append(os.path.join(path, file_name))

    # Create 7z file.
    if (True == need_pw):
        p7zfile = py7zr.SevenZipFile(p7z_name, mode = 'w', password = passwd)
    else:
        p7zfile = py7zr.SevenZipFile(p7z_name, 'w')

    for file_name in file_list:
        print('Compressing', file_name)
        p7zfile.write(file_name)

    # Close 7z file.
    p7zfile.close()

    print('Done.')
# }


# p7z_all_compress - Compress all file.
def p7z_all_compress(need_pw, passwd):
# {
    # Set current directory path.
    dirpath = '.'

    # Create 7z file.
    if (True == need_pw):
        p7zfile = py7zr.SevenZipFile('1_' + p7z_name, mode = 'w', password = passwd)
    else:
        p7zfile = py7zr.SevenZipFile('1_' + p7z_name, 'w')

    # Warning:
    # If you compress the current folder and
    # the package is in this location,
    # the compressed file will contain the package
    # that was created when the state was created.
    p7zfile.writeall(dirpath)

    # Close.
    p7zfile.close()

    print('Done.')
# }


# Main function.
def main():
# {
    # Compress.
    # Example 1: Compress all file by file list.
    p7z_file_compress(True, p7z_passwd)

    # Example 2: Compress all file.
    p7z_all_compress(False, p7z_passwd)

    # Uncompress.
    # Example 4: Extract all file.
    p7z_all_umcompress(False)

    # Example 3: Extract single file.
    p7z_file_uncompress()
# }


# Program entry.
if '__main__' == __name__:
    p7z_name        = 'test.7z'
    p7z_passwd      = '123456'
    file_name       = 'README.md'
    extract_path    = 'et_test'

    main()
