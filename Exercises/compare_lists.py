#!use/bin/python3
lst = [1, 2, 3, 4]
lst2 = [8, 1, 9, 0]
def 
if len(lst) > len(lst2):
    print('lst is larger')
elif len(lst) == len(lst2):
    comparings = []
    for i in range(len(lst)):
        if lst[i] > lst2[i]:
            comparings.append(0)
        elif lst[i] < lst2[i]:
            comparings.append(1)
    if comparings.count(0) > comparings.count(1):
        print("lst is larger")
    elif comparings.count(0) < comparings.count(1):
        print("lst2 is larger")
    else:
        print("equal")
else:
    print("lst2 is larger")
