# Написать функцию по решению квадратных уравнений.[01-11.2-Proc17]
from math import sqrt


def solve_square_equations(a, b, c):
    discriminant = (b ** 2) - 4 * a * c
    print(discriminant)
    if discriminant > 0:
        solution_1 = (-b + sqrt(discriminant)) / (2 * a)
        solution_2 = (-b - sqrt(discriminant)) / (2 * a)
        print(solution_1, solution_2)
    elif discriminant == 0:
        solution = (-b) / (2 * a)
        print(solution)
    else:
        print('The equations has no solutions')



solve_square_equations(3 , -14, -5)
