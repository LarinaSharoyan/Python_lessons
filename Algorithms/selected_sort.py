"""Sorting algorithms/ selected sort"""
def selected_sort(lst):
    """This functions is doing a selected sort"""
    lst2 = []
    while len(lst) != 0:
        lst2.append(max(lst))
        lst.remove(max(lst))
    return lst2
list1 = [5, 3, 5, 6, 0,-9]
sorted_arr = selected_sort(list1)
print(sorted_arr)
