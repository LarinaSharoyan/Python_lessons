st = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
dct = {}
for i in lst:
    if i['item'] not in dct:
        dct[i['item']] = i['amount']
    else:
        dct[i['item']] += i['amount']
print(dct)
