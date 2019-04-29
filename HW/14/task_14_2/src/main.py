from src.matrix_utils.matrix_classes import Matrix
from src.matrix_utils.matrix_funcs import max_matrix, min_matrix, sum_matrix

matrix = Matrix()

print(matrix)
print('max elem', max_matrix(matrix))
print('min elem', min_matrix(matrix))
print('sum elem', sum_matrix(matrix))
