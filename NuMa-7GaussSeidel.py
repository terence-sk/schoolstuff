from numpy import array, diag, diagflat, dot, subtract, linalg, tril, dot



def gauss(A, b, xk1):
    # hodnoty pod diagonalou, tril = lower triangle
    L = tril(A)
    print("Normalna matica\n", A)
    print("Hodnoty pod diagonalou\n", L)
    # tu to uz staci odcitat, hodnoty nad diagonalou dostaneme
    U = A - L
    print("Hodnoty nad diagonalou\n", U)
    xk0 = [0,0,0]
    while True:
        #aktualna
        xk1 = dot(linalg.inv(L), b - dot(U, xk1))

        #print(xk1)
        #kontrola
        if linalg.norm(subtract(xk1, xk0)) <= pow(10, -9):
            return xk1
        #predosla
        xk0 = xk1[:]

    return xk1

equations = array([[4, -1, 2], [2.0, 5.0, 1.0], [1.0, 1.0, -3.0]])
equation_results = [-12.0, 5.0, -4.0]
guesses = [0.0, 0.0, 0.0]

print("Vysledny vektor: ", gauss(equations, equation_results, guesses))
