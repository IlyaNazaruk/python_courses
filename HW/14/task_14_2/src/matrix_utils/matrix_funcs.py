def max_matrix(matrix):
    max_matrix_elem = int(matrix[0][0])
    for row in matrix:
        for elem in row:
            if max_matrix_elem <= int(elem):
                max_matrix_elem = int(elem)
    return max_matrix_elem


def min_matrix(matrix):
    min_matrix_elem = int(matrix[0][0])
    for row in matrix:
        for elem in row:
            if min_matrix_elem >= int(elem):
                min_matrix_elem = int(elem)
    return min_matrix_elem


def sum_matrix(matrix):
    sum_matrix_elem = 0
    for row in matrix:
        for elem in row:
            sum_matrix_elem += elem
    return sum_matrix_elem
