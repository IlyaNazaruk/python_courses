# Дан список чисел. Посчитать сколько раз встречается каждое число.
# Подсказка: для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре использовать метод get()

def count_numbers(numbers):
    counters = {}
    for element in numbers:
        if element in counters:
            counters[element] += 1
        else:
            counters[element] = 1
    return counters


print(count_numbers([1, 2, 3, 4, 1]))
