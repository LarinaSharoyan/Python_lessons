import argparse
import os
import shutil
def adding_properties():
    parser = argparse.ArgumentParser(description="directory name")
    parser.add_argument('directory')
    args = parser.parse_args()
    directory_name = args.directory
    return directory_name


def check_dir_existence(dir_name):
    if not os.path.isdir(dir_name):
        print(f"sorry, but your {dir_name} directory does not exist. Please check.")
        exit()

def get_dir_files(dir_name):
    dir_content = os.listdir(dir_name)
    for file in dir_content:
        current_path = os.getcwd()+file
        file_format = file.split('.')[1]
        m_path = current_path + f"/{file_format[1:]}" + file
        if not os.path.isdir(file_format):
            os.mkdir(file_format)
        shutil.move(current_path, m_path)
dir_name = adding_properties()
check_dir_existence(dir_name)
get_dir_files(dir_name)
