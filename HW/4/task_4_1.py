#Дан список целых чисел.
#Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2

list = [5, 123, 54, -1, 21, -9]
new_list = []
b = 0
while b != len(list):
    new_list.append(list[b] * (-2))
    b += 1
print(new_list)
