# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.
# [02-4.2-ML22]
n = int(input())
matrix = []
list_of_max = []
import random
for row in range(n):
    B = []
    for elem in range(n):
        B.append(int(random.randint(1, 20)))
    matrix.append(B)
for B in matrix:
    print(B)
for i in range(n):
    max_in_row = matrix[i][1]
    for j in range(n):
        if max_in_row <= matrix[i][j]:
            max_in_row = matrix[i][j]
    list_of_max.append(max_in_row)
print()
for i in range(n):
    for j in range(n):
        if i == j :
            elem_diag = matrix[i][j]
            matrix[i][j] = list_of_max[i]
            list_of_max[i] = elem_diag

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print()
