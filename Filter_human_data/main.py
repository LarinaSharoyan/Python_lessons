#!/usr/bin/python
import os.path
def check_file_existence(fname):
    if not os.path.isfile(fname):
        print("Your files does not exists: %s. Please check" %fname)
        return False
    return True

def open_data(file):
    with open(file) as f:
        return f.readlines()
    file.close()

def filter_by_what():
    filter = input("Choose by what you want to filter the data: \n 1. name \n 2. surname \n 3. age \n 4. profession \n your option:  ")
    lst = ['name', 'age', 'surname', 'profession', '1', '2', '3', '4']
    while filter.lower() not in lst:
        filter = input("You must write the number or name of one of these options: \n 1. name \n 2. surname \n 3. age \n 4. profession \n your option:  ")
    return filter.lower()

def create_list_of_dct(f):
    lst = []
    for i in f:
        line = i.strip().split()
        dct = {}
        dct['name'] = line[0]
        dct['surname'] = line[1]
        dct['age'] = line[2]
        dct['profession'] = line[3]
        lst.append(dct)
    return lst

def sort_lst(lst, filter):
    return sorted(lst, key=lambda x: x[filter])

def write_data(file, lst):
    with open(file, "w") as f:
        for i in lst:
            f.write(" ".join(i.values()) + "\n")

def main():
    file1 = "data.txt"
    file2 = "sorted_data.txt"
    fl = check_file_existence(file1)
    fl2 = check_file_existence(file2)
    check_file_existence(file2)
    if not fl or not fl2:
        exit()
    data = open_data(file1)
    filter = filter_by_what()
    lst = create_list_of_dct(data)
    sorted_lst = sort_lst(lst, filter)
    write_data(file2, sorted_lst)

main()
