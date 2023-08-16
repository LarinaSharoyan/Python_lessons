dct = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
sorted_dict = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))
new_dct = {}
for k, v in sorted_dict.items():
    if len(new_dct) != 3:
        new_dct[k] = v
    else:
        break
print(new_dct)
