# Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε — вещественные, ε > 0),
# находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε .
# С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε .  [01-11.3-Proc41]
from math import factorial


def add_part(n, x):
    return ((((-1) ** n) * ((x ** (2 * n + 1))) / factorial(2 * n + 1)))


def math_func(x, e):
    n = 0
    result = 0
    addition = add_part(n, x)
    while abs(addition) >= e:
        n += 1
        result += addition
        addition = add_part(n, x)
    print(n)
    return result


x = int(input('enter the number '))
e = float(input('privedenie '))
print(math_func(x, e))
