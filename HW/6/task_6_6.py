# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего). [02-4.1-ML27]
list_of_numbers = [5, 1, 2, 3, 4, 3, 5, 7, 9, 5, 4, 3, 12, 13, 14, -2, 3, 4]
list_of_rows = []
rows = []
i = 1
len_list = len(list_of_numbers)
while i <= len_list:
    if list_of_numbers[i] > list_of_numbers[i-1] :
        rows.append(list_of_numbers[i-1])
        j = i
        # print(j)
        while list_of_numbers[j-1] < list_of_numbers[j]:
            rows.append(list_of_numbers[j])
            # print(rows)
            j += 1
            if j == len_list:
                break
        i = j
        list_of_rows.append(rows)
    else:
        i += 1
    if i == len_list :
        break
    rows = []
print(list_of_rows)
print(len(list_of_rows), '- количество последовательностей')