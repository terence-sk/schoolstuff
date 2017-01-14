from pprint import pprint
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

A = array([[7, 2, -3], [1, 10, 2], [4, 3, -8]])
b = array([14, 20, 16])
guess = array([0, 0, 0])

pprint(jacobi(A, b, guess))
