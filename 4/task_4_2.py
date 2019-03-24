#Дан список целых чисел. Подсчитать сколько четных чисел в списке

list = [2, -45, 41, 12, 1, 40, 98]
counter = 0
d = 0
while counter != len(list):
    if list[counter] % 2 == 0:
        d += 1
    counter += 1
print(d,' -amount of even numbers')