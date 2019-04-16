# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл. [my-files-t01]

import json
import random


def print_matrix_to_file(filename, matrix):
    with open(filename, "w") as new_file:
        for line in matrix:
            json_line = json.dumps(line)
            new_file.write('{}\n'.format(json_line))


def read_matrix_from_file(filename):
    matrix = []
    with open(filename, "r") as read_file:
        for line in read_file.readlines():
            matrix.append(json.loads(line))
    return matrix


random_matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

print_matrix_to_file('task_10_5_1.txt', random_matrix)
matrix = read_matrix_from_file('task_10_5_1.txt')
for number_1, line in enumerate(matrix):
    for number_2, elem in enumerate(line):
        if elem % 2 == 0:
            matrix[number_1][number_2] = 0

print_matrix_to_file('task_10_5_2.txt', matrix)
