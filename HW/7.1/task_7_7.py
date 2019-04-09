# Описать функцию is_power_n( k , n ) логического типа, возвращающую True,
# если целый параметр k (> 0) является степенью числа n (> 1), и False в противном случае.
# Дано число n (> 1) и набор из 10 целых положительных чисел.
# С помощью функции is_power_n найти количество степеней числа N в данном наборе.[01-11.2-Proc17]

def function(k, n):
    counter = 1
    result = 0
    while k**counter <= n:
        result = k ** counter
        counter += 1
    return (result == n)

k = int(input('chislo'))
n = int(input('chislo for sr'))
result = function(k,n)
if result:
    print('is power of')
else:
    print('is not power off')
list_of_numbers = [1, 2, 64, 29, 8, 81, 14, 23, 16, 243]
length = len(list_of_numbers)
counter = 0
for i in range(length):
    n = list_of_numbers[i]
    res = function(k,n)
    if res:
        counter += 1
print(counter, '- The amount of numbers')