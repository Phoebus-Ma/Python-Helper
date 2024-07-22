###
# Replace all filenames for which the folder is eligible example.
# 
# License - MIT.
###

import os


# Replace all filenames for which the folder is eligible.
def replace_in_filenames(directory, old_str, new_str):
# {
    for filename in os.listdir(directory):
    # {
        if old_str in filename:
            new_filename = filename.replace(old_str, new_str)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
    # }
# }


# Main function
def main():
# {
    folder_path   = 'D:/tulip'
    original_name = 'tulip'
    target_name   = 'tulip_flower'

    replace_in_filenames(folder_path, original_name, target_name)
# }


# Program entry.
if '__main__' == __name__:
    main()
