import numpy as np


def gauss(A, b, x, n):

    L = np.tril(A)
    print("Normalna matica", A)
    print("Hodnoty pod diagonalou", L)
    U = A - L
    print("Hodnoty nad diagonalou", U)
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print(str(i).zfill(3))
        print(x)
    return x

equations = np.array([[7.0, 2.0, -3.0], [1.0, 10.0, 2.0], [4.0, 3.0, -8.0]])
equation_results = [14.0, 20.0, 16.0]
guesses = [0.0, 0.0, 0.0]
n = 25

print(gauss(equations, equation_results, guesses, n))