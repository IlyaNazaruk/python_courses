# В массиве целых чисел с количеством элементов 19
# определить максимальное число и заменить им все четные по значению элементы. [02-4.1-BL19]

list_of_numbers = [1, 42, 94, 84, 72, 12, -8, 79, 41, -48, 23, 11, 43, 14, 63, 54, -21, 24, 90]
number = list_of_numbers[0]
len_of_list = len(list_of_numbers)
for i in range(len_of_list):
    if number <= list_of_numbers[i]:
        number = list_of_numbers[i]
for i in range(len_of_list):
    if list_of_numbers[i] % 2 == 0:
        list_of_numbers[i] = number
print(list_of_numbers)