from functools import reduce
from random import randint
from copy import deepcopy

eps = 10**-7

def dot(a, b):
    return sum([x*y for (x, y) in zip (a, b)])

def norm(vector):
    return dot(vector, vector)**0.5

def scalar_mult(alpha, vector):
    return [alpha * vector[i] for i in range(len(vector))]

def matrix_mult(matrix, vector):
    return [dot(vector, matrix[i]) for i in range(len(vector))]

def random_matrix(n):
    matrix = [[0.] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = randint(-100, 100)
            matrix[j][i] = matrix[i][j]
    return matrix

def sub(a, b):
    return [a[i] - b[i] for i in range(len(a))]

def shifted(matrix):
    shifted_matrix = deepcopy(matrix)
    sigma = sum([abs(matrix[i][i]) for i in range(len(matrix))])
    for i in range(len(shifted_matrix)):
        shifted_matrix[i][i] += sigma
    return sigma, shifted_matrix

def eigen(matrix, sigma=0):
    matrix = deepcopy(matrix)
    iteration = 1
    y = [1 for i in range(len(matrix))]
    old_error = norm(matrix_mult(matrix, y))
    while "calculating":
        u = scalar_mult(1/norm(y), y)
        y = matrix_mult(matrix, u)
        max_lambda = dot(y, u)
        error_vector = sub(matrix_mult(matrix, u),  scalar_mult(max_lambda, u))
        error = norm(error_vector)
        if error < eps:
            print(f"y_0 = {[1 for _ in range(len(matrix))]}")
            print(f"iteration = {iteration}")
            print(f"u = {u}")
            print(f"lambda = {max_lambda - sigma}")
            print(f"error = {error}")
            print(f"error_vector = {error_vector}")
            return max_lambda

        if iteration % 6 == 0:
            old_error = error

        if iteration % 10 == 0 and error > old_error:
            if sigma > 0 :
                print("Unable to calculate the eigenvalue")
                return -1
            sigma, shifted_matrix = shifted(matrix)
            return eigen(shifted_matrix, sigma=sigma)
        iteration += 1

matrix = random_matrix(10)
eigen(matrix)
matrix = [[-1, -2, -4, 6], [-4, 0, 8, 0], [0, 0, 24, 0], [-4, 6, 4, 0]]
eigen(matrix)
matrix = [[-1, -1, 4], [-6, -2, 12], [-9, 3, 4]]
eigen(matrix)
