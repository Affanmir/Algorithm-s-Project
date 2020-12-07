import random
import strassen
import parallel


def multiply(A, B, n):
    R = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                R[i][j] += A[i][k] * B[k][j]
    return R

