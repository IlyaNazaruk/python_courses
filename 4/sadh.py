l = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
key = 0
while key != len(l):
    c = str(len((l)))
    list_keys[key] = list_keys[key] + c

    key += 1

print(l)
