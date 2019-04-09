# Написать функцию принимающая на вход неопределенным
# количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое
# либо среднегеометрическое. Написать программу в виде трех функций.

def geometric_mean(*args):
    result = 1
    length = len(args)
    for i in range(length):
        result *= args[i]
    result = result ** float(1 / length)
    return result


def arithmetic_mean(*args):
    result = 0
    length = len(args)
    for i in range(length):
        result += args[i]
    result = result / length
    return result


def get_means(mean_type, *args):
    if mean_type == 'geometric':
        print('geometric_mean =', geometric_mean(*args))
    elif mean_type == 'arithmetic':
        print('arithmetic mean =', arithmetic_mean(*args))
    else:
        print('ERROR')


args = (1, 2, 3, 4)
mean_type = str(input('enter the type '))
get_means(mean_type, *args)
