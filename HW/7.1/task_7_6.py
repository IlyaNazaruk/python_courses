# Дан массив целых чисел A. Найти суммы положительных и отрицательных элементов массива,
# используя функцию определения суммы. [02-5.1-BL21]
def sum_of_numbers(*numbers):
    positive_list = []
    negative_list = []
    for element in numbers:
        if element > 0:
            positive_list.append(element)
        else:
            negative_list.append(element)
    sum_positive = sum(positive_list)
    sum_negative = sum(negative_list)
    print(sum_positive, sum_negative)


args = [1, 2, 3, -14, -25, 17, -3, 0]
sum_of_numbers(*args)
