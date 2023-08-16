dct1 = {"a": 1, "b": 88, "c": 489}
dct2 = {"k": 2,  "a": 67, "c":10}
new_dct= {}
for k, v in dct1.items():
    if k not in new_dct:
        new_dct[k] = v
    else:
        list(new_dct[k]).append(v)
for k, v in dct2.items():
    if k not in new_dct:
        new_dct[k] = v
    else:
        new_dct[k] = [new_dct[k]]
        new_dct[k].append(v)
print(new_dct)
