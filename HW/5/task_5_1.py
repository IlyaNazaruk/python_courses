# Дана целочисленная матрица размера 5х5. Получить новую матрицу
# путем деления всех элементов данной матрицы на ее наибольший по
# модулю элемент.[02-4.2-ML-17]
import random
A = []
for i in range(5):
    B = []
    for j in range(5):
        B.append(int(random.randint(-20, 20)))
    A.append(B)
for B in A:
    print(B)
max = A[i][j]
for i in range(5):
    for j in range(5):
        if max <= abs(A[i][j]):
            max = abs(A[i][j])
print(max, '-the max number')
print('NEW table')
i = 0
j = 0
for c in range(5):
    for e in range(5):
        d=A[i][j]/max
        print('%.2f'%d, end=' ')
        j += 1
    print()
    i += 1
    j = 0


