###
# Python zip compress test.
# 
# License - MIT
###

import os
import zipfile


# zip_all_umcompress - Unzip the all file.
def zip_all_umcompress(zfile, et_style):
# {
    if (1 == et_style):
        for et_file in zfile.namelist():
            print('Uncompressing', et_file)
            zfile.extract(et_file, path = extract_path)
    else:
        zfile.extractall(path = extract_path)
        print('Decompressed file successfully.')
# }


# zip_file_uncompress - Unzip the specified file.
def zip_file_uncompress(zfile):
# {
    data = zfile.read(file_name)

    print(data.decode('UTF-8'))
# }


# zip_info_get - Gets property information for the specified file in zip.
def zip_info_get(zfile):
# {
    # .
    zinfo = zfile.getinfo(file_name)

    # .
    print('filename:\t',     zinfo.filename)
    print('data_time:\t',    zinfo.date_time)
    print('compress_type:\t',zinfo.compress_type)
    print('compress_size:\t',zinfo.compress_size)
    print('file_size:\t',    zinfo.file_size)
# }


# zip_file_compress - Zip files in a specified folder, excluding subfolder files.
def zip_file_compress():
# {
    # Set current directory path.
    dirpath = '.'

    # Gets all files for the specified folder.
    files = os.listdir(dirpath)

    # Create zip file.
    zfile = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    for file_name in files:
        print('Compressing', file_name)
        zfile.write(file_name)

    # Close zip file.
    zfile.close()
# }


# Compress specified files and subfolders.
def zip_dir_compress():
# {
    # File list.
    file_list = []

    # Set current directory path.
    dirpath = '.'

    # Get current path all file.
    for path, dirnames, filenames in os.walk(dirpath):

        for file_name in filenames:
           file_list.append(os.path.join(path, file_name))

    # Create zip file.
    new_zip = 'dir_' + zip_name
    zfile = zipfile.ZipFile(new_zip, 'w', zipfile.ZIP_DEFLATED)

    for file_name in file_list:
        print('Compressing', file_name)
        zfile.write(file_name)

    # Close zip file.
    zfile.close()
# }


# Main function.
def main():
# {
    # 1.Zip files in a specified folder.
    zip_file_compress()

    # Open zip file.
    zfile_r = zipfile.ZipFile(zip_name, 'r')

    # 2.Gets property information.
    zip_info_get(zfile_r)

    # 3.Unzip the specified file.
    zip_file_uncompress(zfile_r)

    # 4.Unzip the all file.
    zip_all_umcompress(zfile_r, 0)

    # Close zip file.
    zfile_r.close()

    # 5.Compress specified files and subfolders.
    zip_dir_compress()
# }


# Program entry.
if '__main__' == __name__:
    zip_name        = 'test.zip'
    file_name       = 'README.md'
    extract_path    = 'et_test'

    main()
