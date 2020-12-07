import random


def addition(x, y):
    return [[x[row][col] + y[row][col]
             for col in range(len(x[row]))] for row in range(len(x))]


def subtraction(x, y):
    return [[x[row][col] - y[row][col]
             for col in range(len(x[row]))] for row in range(len(x))]


def default(x, y):
    matrix = [[x[0][0] * y[0][0] + x[0][1] * y[1][0], x[0][0] * y[0][1] + x[0][1] * y[1][1]],
              [x[1][0] * y[0][0] + x[1][1] * y[1][0], x[1][0] * y[0][1] + x[1][1] * y[1][1]]]

    return matrix


def split(matrix):
    n = len(matrix)
    mid = n // 2
    a = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    b = [[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
    c = [[matrix[i][j] for j in range(mid, n)] for i in range(mid)]
    d = [[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return a, c, b, d


def strassen(x, y):
    if len(x) == 2:
        return default(x, y)

    # Splitting the matrices into quadrants. This will be done recursively
    # untill the base case is reached.

    A, B, C, D = split(x)
    E, F, G, H = split(y)

    p1 = strassen(A, subtraction(F, H))
    p2 = strassen(addition(A, B), H)
    p3 = strassen(addition(C, D), E)
    p4 = strassen(D, subtraction(G, E))
    p5 = strassen(addition(A, D), addition(E, H))
    p6 = strassen(subtraction(B, D), addition(G, H))
    p7 = strassen(subtraction(A, C), addition(E, F))

    c11 = addition(subtraction(addition(p5, p4), p2), p6)
    c12 = addition(p1, p2)
    c21 = addition(p3, p4)
    c22 = subtraction(subtraction(addition(p1, p5), p3), p7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(c12)):
        new_matrix.append(c11[i] + c12[i])
    for i in range(len(c22)):
        new_matrix.append(c21[i] + c22[i])
    return new_matrix

