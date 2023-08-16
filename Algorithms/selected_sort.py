lst = [5, 3, 5, 6, 0,-9]
lst2 = []
while len(lst) != 0:
    lst2.append(max(lst))
    lst.remove(max(lst))
print(lst2)
