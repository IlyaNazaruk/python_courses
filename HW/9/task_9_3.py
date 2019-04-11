# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.

def decor(func):
    def upgrade(n):
        list_1 = func(n)
        list_2 = []
        for number in list_1:
            if number % 2 != 0:
                list_2.append(number)
        return list_2

    return upgrade


@decor
def enter_the_list(n):
    from random import randint
    list_of_numbers = [randint(1, 100) for i in range(n)]
    return list_of_numbers


n = int(input('asdq'))
print(enter_the_list(n))

# def decor(func):
#     def upgrade(result_1):
#         result_1 =result_1 * 3
#
#         return func(result_1)
#     return upgrade
#
# @decor
# def function(number):
#     result = number * 2
#     return result
#
#
# print(function(3))
