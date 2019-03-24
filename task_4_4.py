#Дан список. Создать новый список, сдвинутый на 1 элемент влево
#Пример: 1 2 3 4 5 ->  2 3 4 5 1

list = [2, 4, 6, 8, 10, 12]
new_list = []
counter = 0
a = len(list)
while counter != a - 1:
    new_list.append(list[counter+1])
    counter += 1
new_list.append(list[0])
print(new_list)