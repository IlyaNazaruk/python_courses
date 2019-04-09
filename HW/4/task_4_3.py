#Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
#(подсказка: создается новый ключ с цифрой в конце, старый удаляется)

l = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
key = 0
new_list = {}
list_keys = list(l.keys())
list_values = list(l.values())
while key != len(l):
    c = str(len(list_keys[key]))
    list_keys[key] = list_keys[key] + c
    new_list[list_keys[key]] = list_values[key]
    key += 1
print(new_list)

