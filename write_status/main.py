"""
os is to chec kfile existence
sys is for exit()
"""
import os
import sys

def check_dir_existence(dir_name):
    """
    Check if the specified directory exists.
    Args:
        dir_name (str): The name of the directory to check.
    """
    if not os.path.isdir(dir_name):
        print(f"There's no such {dir_name} directory")
        sys.exit()

def check_file_existence(filename):
    """
    Check if the specified file exists.
    Args:
        filename (str): The name of the file to check.
    """
    if not os.path.isfile(filename):
        print(f"{filename} file doesn't exist.")
        sys.exit()

def get_status_files(directory_name):
    """
    Get status information from files in the specified directory.
    Args:
        directory_name (str): The name of the directory to search for files.
    Returns:
        dict: A dictionary containing filenames as keys and their corresponding status as values.
    """
    data = {}
    os.chdir(directory_name)
    # Get a list of files in the directory
    files = list(os.listdir('.'))
    for file in files:
        with open(file, encoding="utf-8") as my_file:
            line = my_file.readline().strip().split(": ")
            # Check if the line indicates status is "PASS" or "FILL"
            if line[0] == 'status' and line[1] in ["PASS", "FILL"]:
                data[file] = line[1]
    return dict(sorted(data.items()))

def write_results(filename, data):
    """
    Write the results to a file.
    """
    os.chdir("../")
    with open(filename, "w", encoding="utf-8") as results:
        for f_name, arg in data.items():
            results.write(f"{f_name} => status: {arg}\n")

def main():
    """All functions collected here!"""
    results_file = "result.txt"
    directory = "files"
    # Check if the specified directory exists
    check_dir_existence(directory)
    # Check if the specified results file exists
    check_file_existence(results_file)
    # Get status information from files in the directory
    data = get_status_files(directory)
    # Write the results to the specified results file
    write_results(results_file, data)

if __name__ == "__main__":
    main()
