###
# Python tar compress/umcompress example.
# 
# License - MIT.
###

import os
import tarfile


# tar_xz_uncompress - Uncompress to xz file.
def tar_xz_uncompress():
# {
    new_name = tar_name + '.xz'
    new_path = extract_path + '_xz'

    with tarfile.open(new_name, 'r:xz') as tfile:
        tfile.extractall(path = new_path)
# }


# tar_xz_compress - Compress to xz file.
def tar_xz_compress():
# {
    fpath = os.getcwd()

    new_name = tar_name + '.xz'

    with tarfile.open(new_name, 'w:xz') as tfile:
        tfile.format = tarfile.GNU_FORMAT
        tfile.add(fpath, os.path.basename(fpath))
# }


# tar_bz2_uncompress - Uncompress to bz2 file.
def tar_bz2_uncompress():
# {
    new_name = tar_name + '.bz2'
    new_path = extract_path + '_bz2'

    with tarfile.open(new_name, 'r:bz2') as tfile:
        tfile.extractall(path = new_path)
# }


# tar_bz2_compress - Compress to bz2 file.
def tar_bz2_compress():
# {
    fpath = os.getcwd()

    new_name = tar_name + '.bz2'

    with tarfile.open(new_name, 'w:bz2') as tfile:
        tfile.format = tarfile.GNU_FORMAT
        tfile.add(fpath, os.path.basename(fpath))
# }


# tar_gz_uncompress - Uncompress to gz file.
def tar_gz_uncompress():
# {
    new_name = tar_name + '.gz'
    new_path = extract_path + '_gz'

    with tarfile.open(new_name, 'r:gz') as tfile:
        tfile.extractall(path = new_path)
# }


# tar_gz_compress - Compress to gz file.
def tar_gz_compress():
# {
    fpath = os.getcwd()

    new_name = tar_name + '.gz'

    with tarfile.open(new_name, 'w:gz') as tfile:
        tfile.format = tarfile.GNU_FORMAT
        tfile.add(fpath, os.path.basename(fpath))
# }


# tar_info - Gets information about the specified file in the tar file.
def tar_info():
# {
    with tarfile.open(tar_name, 'r') as tfile:
        # Get all file names in tar.
        file_list = tfile.getnames()

        for fname in file_list:
            print(fname)

        # Gets property information for the specified file.
        try:
            query_name = os.path.basename(os.getcwd()) + '/' + file_name
            file_info = tfile.getmember(name = query_name)

            print('name', file_info.name)
            print('size', file_info.size)
            print('mtime', file_info.mtime)
        except:
            pass
# }


# tar_unpack - Unpack a tar file.
def tar_unpack():
# {
    with tarfile.open(tar_name, 'r') as tfile:
        tfile.extractall(path = extract_path)
# }


# tar_pack - Package a tar file.
def tar_pack():
# {
    fpath = os.getcwd()

    with tarfile.open(tar_name, 'w') as tfile:
        tfile.format = tarfile.GNU_FORMAT
        tfile.add(fpath, os.path.basename(fpath))
# }


# Main function.
def main():
# {
    # Example 1: Package a tar file.
    tar_pack()

    # Example 2: Unpack a tar file.
    tar_unpack()

    # Example 3: Gets information about the specified file in the tar file.
    tar_info()

    # Example 4: Compress to gz file.
    tar_gz_compress()

    # Example 5: Uncompress to gz file.
    tar_gz_uncompress()

    # Example 6: Compress to bz2 file.
    tar_bz2_compress()

    # Example 7: Uncompress to bz2 file.
    tar_bz2_uncompress()

    # Example 8: Compress to xz file.
    tar_xz_compress()

    # Example 9: Uncompress to xz file.
    tar_xz_uncompress()
# }


# Program entry.
if '__main__' == __name__:
    tar_name        = 'test.tar'
    file_name       = 'README.md'
    extract_path    = 'et_test'

    main()
