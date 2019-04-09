# Рассчитать значение х определив и использовав необходимую функции. [02-5.1-BL01]

from math import sqrt


def the_equation(*args):
    result = 0
    for element in args:
        result += sqrt(float(element)) + element / 2
    return result


enter = the_equation(5, 12, 19)
enter = float('{:.3f}'.format(enter))
print(enter)
