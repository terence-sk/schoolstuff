from numpy import array, diag, diagflat, dot, subtract, linalg


# A = priklad, b = vysledky, xk1 = tip
def jacobi(A, b, xk1):

    xk0 = [0, 0, 0]

    # D = diagonala matice A (priklad)
    D = diag(A)
    # Odcitame od matice A hodnoty na diagonale
    R = A - diagflat(D)

    # numpy.dot = nasobenie matic
    while True:

        #aktualna hodnota
        xk1 = (b - dot(R, xk1)) / D

        # kontrolujeme normu... presnost na 9 miest
        if linalg.norm(subtract(xk1, xk0)) <= pow(10, -9):
            return xk1

        # tu si ulozim predoslu hodnotu
        xk0 = xk1[:]

A = array([[4, -1, 2], [2, 5, 1], [1, 1, -3]])
b = array([-12, 5, -4])
guess = array([0, 0, 0])

print(jacobi(A, b, guess))
