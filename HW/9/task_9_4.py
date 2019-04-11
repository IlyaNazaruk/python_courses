# Создать универсальны декоратор, который меняет порядок аргументов в функции на противоположный.
import random


def decor(func):
    def upgrade(*args):
        new_list = args[::-1]
        return func(*new_list)

    return upgrade


@decor
def my_func(*args):
    return args


@decor
def abc(a, b, c):
    print('a', a)
    print('b', b)
    print('c', c)


abc(1, 2, 3)
args = [1, 14, 15, 87]
print(my_func(*args))
