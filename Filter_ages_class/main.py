class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
def get_data(fname):
    data = []
    with open(fname) as f:
        lines = f.readlines()
        for i in lines:
            line = i.strip().split()
            data.append(line)
    f.close()
    return data
def create_objects(data):
    obj_list = []
    for i in data:
        obj_list.append(Human(i[0], i[1], i[2]))
    return obj_list
def filter_objects(obj_list):
    return sorted(obj_list, key=lambda x: x.age)

def print_objects(lst):
    for i in lst:
        print(i.name, i.surname, i.age)
data = get_data("person_info.txt")
obj_list = create_objects(data)
sorted_list = filter_objects(obj_list)
print_objects(sorted_list)
