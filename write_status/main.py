import os
def check_directory_existence
def write_data(file_dir):
data = {}
os.chdir("files")
files = [f for f in os.listdir('.')]
for file in files:
    with open(file) as my_file:
        line = my_file.readline().strip().split(": ")
        if line[0] == 'status' and line[1] in ["PASS", "FILL"]:
            data[file] = line[1]
os.chdir("../")
with open("results.txt", "w") as results:
    for f_name, arg in data.items():
        results.write(f"{f_name} => status: {arg} \n")

    
